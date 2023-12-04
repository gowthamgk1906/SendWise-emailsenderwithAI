# urls.py

from django.urls import path
from .views import AIChatView

urlpatterns = [
    path('chatbot/', AIChatView.as_view(), name='ai_chat'),
]
