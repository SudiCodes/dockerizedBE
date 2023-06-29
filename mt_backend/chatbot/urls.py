from chatbot.views import ChatbotView
from django.urls import path


urlpatterns = [
    path('chat/', ChatbotView.as_view(), name='chatbot')
]
