from django.http import JsonResponse
from django.shortcuts import render
from .chatbot import get_chatbot

bot = get_chatbot()

def index(request):
    return render(request, 'chatbotapp/index.html')

def get_chatbot_response(request):
    if request.method == 'GET':
        user_text = request.GET.get('userMessage', '')
        response = bot.get_response(user_text)
        return JsonResponse({'response': str(response)})