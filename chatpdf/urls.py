# backend/chatpdf/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView  # Import TokenRefreshView
from .views import (
    RegisterView,
    LoginView,
    GoogleLogin,
    PasswordResetRequest,
    PasswordResetConfirm,
    UploadPDFView,
    ChatView,
    ConversationHistoryView,
    MessageHistoryView,
    ConversationDetailView,
    ServePDFView,
    SummaryMessageByAiView,
    download_summary
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('google-login/', GoogleLogin.as_view(), name='google_login'),
    path('password-reset/',PasswordResetRequest.as_view(), name='password_reset_request'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint để refresh token
    path('upload-pdf/', UploadPDFView.as_view(), name='upload_pdf'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('history/', ConversationHistoryView.as_view(), name='history'),
    path('history/<int:conversation_id>/messages/', MessageHistoryView.as_view(), name='message_history'),
    path('history/<int:conversation_id>/', ConversationDetailView.as_view(), name='conversation_detail'),
    path('media/pdfs/<int:pdf_id>/', ServePDFView.as_view(), name='serve_pdf'),
    path('summary/', SummaryMessageByAiView.as_view(), name='summary_messages'),
    path('media/summaries/<str:filename>', download_summary, name='download_summary'),
]