# backend/chatpdf/models.py
from django.db import models
from django.contrib.auth.models import User

class PDFDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.ForeignKey(PDFDocument, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default="New Conversation")

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    is_user = models.BooleanField(default=True)
    model_used = models.CharField(
        max_length=10,
        choices=[
            ('gemini', 'Gemini'),
            ('deepseek', 'DeepSeek'),  # Thêm DeepSeek vào danh sách
            ('llama', 'Llama'),
            ('gemma', 'Gemma'),       # Thêm Gemma nếu cần
        ],
        default='gemini'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:50]}..."