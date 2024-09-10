from django.shortcuts import render
from .models import Intent, Entities, UserMessage
from .nlp import extract_intent_and_entities
#from chat.nlp import extract_intent_and_entities

def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        intent, entities = extract_intent_and_entities(user_message)
        UserMessage.objects.create(message=user_message, intent=intent, entities=entities)
        return render(request, 'accounts/response.html', {'intent': intent, 'entities': entities})
    return render(request, 'accounts/chatbot.html')