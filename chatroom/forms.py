from django import forms
from .models import ChatRoom


class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ["name"]


class MessageForm(forms.Form):
    message = forms.CharField(label="Message", max_length=1000)
