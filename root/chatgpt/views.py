from django.shortcuts import render
from django.http import JsonResponse
import openai

# Установите свой API-токен
openai.api_key = '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'


def chatgpt(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты мой ассистент, который всегда отвечает на русском языке"},
                {"role": "user", "content": message},
            ]
        )
    
        response = response.choices[0].message.content.strip()

        return JsonResponse({
            'message': message,
            'response': response,
        })
    

    return render(request, 'chatgpt.html')

