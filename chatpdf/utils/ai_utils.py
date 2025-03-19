import google.generativeai as genai
from openai import OpenAI
from django.conf import settings
import redis
import requests


# Kết nối tới Redis
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True 
)

def get_gemini_response(conversation_id: int, user_message: str, pdf_text: str = None):
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        # Nếu pdf_text được gửi (lần đầu), lưu vào Redis
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        # Lấy ngữ cảnh từ Redis
        context = redis_client.get(f"pdf_context:{conversation_id}")
        if not context:
            return "Error: No PDF context available for this conversation."

        # Gửi yêu cầu đến model với ngữ cảnh và tin nhắn người dùng
        response = model.generate_content(f"{context}\n\nUser: {user_message}")
        return response.text
    except Exception as e:
        print(f"Gemini API error: {str(e)}")
        return "Sorry, I couldn't process your request with Gemini at this time."


def get_deepseek_response(conversation_id: int, user_message: str, pdf_text: str = None):
    try:
        # Nếu pdf_text được gửi (lần đầu), lưu vào Redis
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        # Lấy ngữ cảnh từ Redis
        context = redis_client.get(f"pdf_context:{conversation_id}")
        if not context:
            return "Error: No PDF context available for this conversation."

        # Sử dụng OpenRouter API với key từ OpenRouter
        client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,  # Thay bằng API key từ OpenRouter
            base_url="https://openrouter.ai/api/v1"  # Endpoint của OpenRouter
        )
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",  # Model miễn phí DeepSeek v3
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_message},
            ],
            max_tokens=10000
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"DeepSeek v3 (OpenRouter) error: {str(e)}")
        return "Sorry, I couldn't process your request with DeepSeek v3 at this time."

# Xóa ngữ cảnh từ Redis
def clear_context(conversation_id: int):
    redis_client.delete(f"pdf_context:{conversation_id}")

def get_llama_response(conversation_id: int, user_message: str, pdf_text: str = None):
    try:
        # Nếu pdf_text được gửi (lần đầu), lưu vào Redis
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        print("id hội thoại :", conversation_id)
        # Lấy ngữ cảnh từ Redis
        context = redis_client.get(f"pdf_context:{conversation_id}")
        if not context:
            return "Error: No PDF context available for this conversation."

        # Sử dụng OpenRouter API với key từ OpenRouter
        client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,  # Thay bằng API key từ OpenRouter
            base_url="https://openrouter.ai/api/v1"  # Endpoint của OpenRouter
        )
        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",  # Model miễn phí DeepSeek v3
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_message},
            ],
            max_tokens=10000
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"Llama (OpenRouter) error: {str(e)}")
        return "Sorry, I couldn't process your request with Llama at this time."
def get_qwen_response(conversation_id: int, user_message: str, pdf_text: str = None):
    try:
        # Nếu pdf_text được gửi (lần đầu), lưu vào Redis
        if pdf_text:
            redis_client.set(f"pdf_context:{conversation_id}", pdf_text)

        print("id hội thoại :", conversation_id)
        # Lấy ngữ cảnh từ Redis
        context = redis_client.get(f"pdf_context:{conversation_id}")
        if not context:
            return "Error: No PDF context available for this conversation."

        # Sử dụng OpenRouter API với key từ OpenRouter
        client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,  # Thay bằng API key từ OpenRouter
            base_url="https://openrouter.ai/api/v1"  # Endpoint của OpenRouter
        )
        response = client.chat.completions.create(
            model="qwen/qwq-32b:free",  # Model miễn phí DeepSeek v3
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_message},
            ],
            max_tokens=10000
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"qwen (OpenRouter) error: {str(e)}")
        return "Sorry, I couldn't process your request with qwen at this time."

def get_gemma_response(pdf_text, user_message):
    try:
        API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b"
        HEADERS = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"}

        data = {
            "inputs": f"{pdf_text}\n\nUser: {user_message}"
        }

        response = requests.post(API_URL, headers=HEADERS, json=data)
        response_json = response.json()

        if "error" in response_json:
            print(f"Gemma API error: {response_json['error']}")
            return "Sorry, I couldn't process your request with Gemma at this time."

        return response_json[0]["generated_text"]
    except Exception as e:
        print(f"Gemma API error: {str(e)}")
        return "Sorry, I couldn't process your request with Gemma at this time."