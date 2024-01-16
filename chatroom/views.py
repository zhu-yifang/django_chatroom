from django.shortcuts import render
from .models import ChatRoom, Message

def chat_room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat_room_list.html', {'rooms': rooms})

def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    messages = Message.objects.filter(room=room).order_by('-timestamp')
    return render(request, 'chat_room.html', {'room': room, 'messages': messages})
