# backend/chatpdf/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    is_plus = models.BooleanField(default=False)
    plus_expiry = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

class MessageLimit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pdf = models.ForeignKey('PDFDocument', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    message_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'pdf', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.pdf.title} - {self.date}"

class PDFDocument(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Conversation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
            ('deepseek', 'DeepSeek'),
            ('llama', 'Llama'),
            ('qwen', 'Qwen'),
            ('gemma', 'Gemma'),
        ],
        default='gemini'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:50]}..."
    
class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Số tiền thanh toán
    payment_date = models.DateTimeField(auto_now_add=True)  # Ngày thanh toán
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
        default='pending'
    )
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('credit_card', 'Credit Card'),
            ('paypal', 'PayPal'),
            ('bank_transfer', 'Bank Transfer'),
        ],
        default='credit_card'
    )
    transaction_id = models.CharField(max_length=100, blank=True, null=True)  # ID giao dịch (nếu có)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.payment_date}"