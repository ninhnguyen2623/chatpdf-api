import google.generativeai as genai
from openai import OpenAI
from django.conf import settings
import redis
import requests
from ..models import Message  # Import model Message để truy vấn lịch sử

# Kết nối tới Redis
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True 
)

# Hàm lấy lịch sử tin nhắn từ DB hoặc Redis
def get_conversation_history(conversation_id: int) -> str:
    # Kiểm tra Redis trước
    history_key = f"chat_history:{conversation_id}"
    cached_history = redis_client.get(history_key)
    if cached_history:
        return cached_history

    # Nếu không có trong Redis, lấy 10 tin nhắn cuối từ DB
    messages = Message.objects.filter(conversation_id=conversation_id).order_by('-created_at')[:10][::-1]  # Lấy 10 tin nhắn cuối và đảo lại
    history = "\n".join(
        [f"{'User' if msg.is_user else 'AI'}: {msg.content}" for msg in messages]
    )
    
    # Lưu vào Redis để sử dụng sau
    redis_client.set(history_key, history)
    return history

# Hàm cập nhật lịch sử sau mỗi tin nhắn mới
def update_conversation_history(conversation_id: int, role: str, content: str):
    history_key = f"chat_history:{conversation_id}"
    current_history = redis_client.get(history_key) or ""
    updated_history = f"{current_history}\n{role}: {content}" if current_history else f"{role}: {content}"
    redis_client.set(history_key, updated_history)

def get_gemini_response(conversation_id: int, user_message: str, pdf_text: str = None):
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        # Nếu pdf_text được gửi (lần đầu), lưu vào Redis
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        # Lấy ngữ cảnh PDF từ Redis
        pdf_context = redis_client.get(f"pdf_context:{conversation_id}")
        if not pdf_context:
            return "Error: No PDF context available for this conversation."

        # Lấy lịch sử hội thoại
        chat_history = get_conversation_history(conversation_id)

        # Tạo ngữ cảnh đầy đủ: PDF + lịch sử + tin nhắn mới
        full_context = f"{pdf_context}\n\n--- Previous Conversation ---\n{chat_history}\n\nUser: {user_message}"

        # Gửi yêu cầu đến model
        response = model.generate_content(full_context)
        
        # Cập nhật lịch sử với tin nhắn mới
        update_conversation_history(conversation_id, "User", user_message)
        update_conversation_history(conversation_id, "AI", response.text)

        return response.text
    except Exception as e:
        print(f"Gemini API error: {str(e)}")
        return "Sorry, I couldn't process your request with Gemini at this time."

def get_deepseek_response(conversation_id: int, user_message: str, pdf_text: str = None):
    try:
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        pdf_context = redis_client.get(f"pdf_context:{conversation_id}")
        if not pdf_context:
            return "Error: No PDF context available for this conversation."

        chat_history = get_conversation_history(conversation_id)

        client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",
            messages=[
                {"role": "system", "content": f"{pdf_context}\n\n--- Previous Conversation ---\n{chat_history}"},
                {"role": "user", "content": user_message},
            ],
            max_tokens=10000
        )
        
        # Cập nhật lịch sử
        update_conversation_history(conversation_id, "User", user_message)
        update_conversation_history(conversation_id, "AI", response.choices[0].message.content)

        return response.choices[0].message.content
    except Exception as e:
        print(f"DeepSeek v3 (OpenRouter) error: {str(e)}")
        return "Sorry, I couldn't process your request with DeepSeek v3 at this time."

def get_llama_response(conversation_id: int, user_message: str, pdf_text: str = None):
    try:
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        pdf_context = redis_client.get(f"pdf_context:{conversation_id}")
        if not pdf_context:
            return "Error: No PDF context available for this conversation."

        chat_history = get_conversation_history(conversation_id)

        client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )
        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=[
                {"role": "system", "content": f"{pdf_context}\n\n--- Previous Conversation ---\n{chat_history}"},
                {"role": "user", "content": user_message},
            ],
            max_tokens=10000
        )
        
        # Cập nhật lịch sử
        update_conversation_history(conversation_id, "User", user_message)
        update_conversation_history(conversation_id, "AI", response.choices[0].message.content)

        return response.choices[0].message.content
    except Exception as e:
        print(f"Llama (OpenRouter) error: {str(e)}")
        return "Sorry, I couldn't process your request with Llama at this time."

def get_qwen_response(conversation_id: int, user_message: str, pdf_text: str = None):
    try:
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        pdf_context = redis_client.get(f"pdf_context:{conversation_id}")
        if not pdf_context:
            return "Error: No PDF context available for this conversation."

        chat_history = get_conversation_history(conversation_id)

        client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )
        response = client.chat.completions.create(
            model="qwen/qwq-32b:free",
            messages=[
                {"role": "system", "content": f"{pdf_context}\n\n--- Previous Conversation ---\n{chat_history}"},
                {"role": "user", "content": user_message},
            ],
            max_tokens=10000
        )
        
        # Cập nhật lịch sử
        update_conversation_history(conversation_id, "User", user_message)
        update_conversation_history(conversation_id, "AI", response.choices[0].message.content)

        return response.choices[0].message.content
    except Exception as e:
        print(f"Qwen (OpenRouter) error: {str(e)}")
        return "Sorry, I couldn't process your request with Qwen at this time."

def get_gemma_response(conversation_id: int, user_message: str, pdf_text: str = None):  # Thêm conversation_id
    try:
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        pdf_context = redis_client.get(f"pdf_context:{conversation_id}")
        if not pdf_context:
            return "Error: No PDF context available for this conversation."

        chat_history = get_conversation_history(conversation_id)

        API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b"
        HEADERS = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"}

        full_context = f"{pdf_context}\n\n--- Previous Conversation ---\n{chat_history}\n\nUser: {user_message}"
        data = {"inputs": full_context}

        response = requests.post(API_URL, headers=HEADERS, json=data)
        response_json = response.json()

        if "error" in response_json:
            print(f"Gemma API error: {response_json['error']}")
            return "Sorry, I couldn't process your request with Gemma at this time."

        ai_response = response_json[0]["generated_text"]
        
        # Cập nhật lịch sử
        update_conversation_history(conversation_id, "User", user_message)
        update_conversation_history(conversation_id, "AI", ai_response)

        return ai_response
    except Exception as e:
        print(f"Gemma API error: {str(e)}")
        return "Sorry, I couldn't process your request with Gemma at this time."

def clear_context(conversation_id: int):
    redis_client.delete(f"pdf_context:{conversation_id}")
    redis_client.delete(f"chat_history:{conversation_id}")  # Xóa cả lịch sử chat