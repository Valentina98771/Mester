from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import PrivateMessage
from chat.serializers import MessageSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = PrivateMessage.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def chat_view(request):
    if request.method == "GET":
        return render(request, 'chat/chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})

def message_view(request, sender, receiver):
    if request.method == "GET":
        return render(request, "chat/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': PrivateMessage.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   PrivateMessage.objects.filter(sender_id=receiver, receiver_id=sender)})
