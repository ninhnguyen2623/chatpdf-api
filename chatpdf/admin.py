# backend/chatpdf/admin.py
from django.contrib import admin
from .models import User, PDFDocument, Conversation, Message, MessageLimit, Payment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_plus', 'plus_expiry')
    list_filter = ('is_plus',)
    search_fields = ('username', 'email')

@admin.register(MessageLimit)
class MessageLimitAdmin(admin.ModelAdmin):
    list_display = ('user', 'pdf', 'date', 'message_count')
    list_filter = ('date', 'user')
    search_fields = ('user__username', 'pdf__title')

@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title',)

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'pdf', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'content', 'is_user', 'model_used', 'created_at')
    list_filter = ('is_user', 'model_used', 'created_at')
    search_fields = ('content',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_date', 'payment_status', 'payment_method', 'transaction_id')
    list_filter = ('payment_status', 'payment_method', 'payment_date')
    search_fields = ('user__username', 'transaction_id')
    readonly_fields = ('payment_date',)