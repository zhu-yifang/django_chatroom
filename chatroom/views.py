from django.shortcuts import get_object_or_404, render, redirect
from .models import ChatRoom, ChatMessage
from .forms import ChatRoomForm, MessageForm
from django.contrib.auth.decorators import login_required


def chat_room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, "chatroom/chat_room_list.html", {"rooms": rooms})


def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    chat_messages = ChatMessage.objects.filter(room=room).order_by("timestamp")
    return render(
        request,
        "chatroom/chat_room.html",
        {"room": room, "chat_messages": chat_messages},
    )


def create_room(request):
    if request.method == "POST":
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("chat_room_list")
    else:
        form = ChatRoomForm()
    return render(request, "chatroom/create_room.html", {"form": form})
