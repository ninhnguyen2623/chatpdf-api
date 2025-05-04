# chatpdf/serializers.py

from rest_framework import serializers
from .models import PDFDocument, Conversation, Message
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_plus', 'plus_expiry']

class PDFDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = ['id', 'title', 'file', 'uploaded_at']

class ConversationSerializer(serializers.ModelSerializer):
    # Thêm trường pdf_url
    pdf_url = serializers.SerializerMethodField()  

    class Meta:
        model = Conversation
        fields = ['id', 'title', 'created_at', 'pdf', 'pdf_url']

    def get_pdf_url(self, obj):
        request = self.context.get('request')
        if obj.pdf and request:
            return request.build_absolute_uri(f"/api/media/pdfs/{obj.pdf.id}/")
        return None

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'is_user', 'model_used', 'created_at']