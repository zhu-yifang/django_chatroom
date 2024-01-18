from django.shortcuts import render, redirect
from .models import ChatRoom, Message
from .forms import ChatRoomForm


def chat_room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, "chatroom/chat_room_list.html", {"rooms": rooms})


def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    messages = Message.objects.filter(room=room).order_by("-timestamp")
    return render(request, "chatroom/chat_room.html", {"room": room, "messages": messages})


def create_room(request):
    if request.method == "POST":
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("chat_room_list")
    else:
        form = ChatRoomForm()
    return render(request, "chatroom/create_room.html", {"form": form})
