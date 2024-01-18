from django.shortcuts import render, redirect
from .models import ChatRoom, ChatMessage
from .forms import ChatRoomForm, MessageForm
from django.contrib.auth.decorators import login_required


def chat_room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, "chatroom/chat_room_list.html", {"rooms": rooms})


def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    chat_messages = ChatMessage.objects.filter(room=room).order_by("-timestamp")
    return render(
        request, "chatroom/chat_room.html", {"room": room, "chat_messages": chat_messages}
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


@login_required
def post_message(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = room
            message.user = request.user
            message.save()
            return redirect(
                "chat_room", room_id=room_id
            )  # Redirect back to the chat room
    else:
        form = MessageForm()
    return redirect(
        "chat_room", room_id=room_id
    )  # Redirect if not a POST request or form is not valid
