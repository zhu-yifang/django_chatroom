from django import forms
from .models import ChatRoom, ChatMessage


class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ["name"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ["content"]  # Assuming your ChatMessage model has a 'content' field
