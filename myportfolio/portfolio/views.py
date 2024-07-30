# portfolio/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        send_to_telegram(name, email, message)
        
        return HttpResponse("Thank you for your message. I'll mail you as soon as possible.")
    return render(request, 'index.html')

def send_to_telegram(name, email, message):
    bot_token = '7316481474:AAFzecpJqMF3AZQqwAvUGVvwClCpzXGeJVw'
    chat_id = '1523086010'
    text = f"New Contact Form Submission:\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    
    requests.post(url, data=payload)
