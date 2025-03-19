# backend/chatpdf/urls.py
from django.urls import path
from .views import RegisterView, LoginView, UploadPDFView, ChatView, ConversationHistoryView, MessageHistoryView, ConversationDetailView,ServePDFView,SummaryMessageByAiView, download_summary

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload-pdf/', UploadPDFView.as_view(), name='upload_pdf'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('history/', ConversationHistoryView.as_view(), name='history'),
    path('history/<int:conversation_id>/messages/', MessageHistoryView.as_view(), name='message_history'),  # Thêm route mới
    path('history/<int:conversation_id>/', ConversationDetailView.as_view(), name='conversation_detail'),  # Thêm route
    path('media/pdfs/<int:pdf_id>/', ServePDFView.as_view(), name='serve_pdf'),
    path('summary/', SummaryMessageByAiView.as_view(), name='summary_messages'),
    path('media/summaries/<str:filename>', download_summary, name='download_summary'),
]