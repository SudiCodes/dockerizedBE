from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime


# Create your views here.


class ChatbotView(APIView):
    def get(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return Response(f"Hello! The current time is: {current_time}")


class BotobotView(APIView):
    pass
