from django.test import TestCase
from chatroom.models import ChatRoom


class ChatRoomModelTest(TestCase):
    def setUp(self):
        ChatRoom.objects.create(name="Test Room")

    def test_chatroom_creation(self):
        room = ChatRoom.objects.get(name="Test Room")
        self.assertEqual(room.name, "Test Room")

    def test_chatroom_str(self):
        room = ChatRoom.objects.get(name="Test Room")
        self.assertEqual(str(room), "Test Room")


from django.contrib.auth.models import User
from chatroom.models import ChatMessage, ChatRoom


class ChatMessageModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        room = ChatRoom.objects.create(name="Test Room")
        ChatMessage.objects.create(room=room, user=user, content="Hello World")

    def test_chatmessage_creation(self):
        message = ChatMessage.objects.get(content="Hello World")
        self.assertEqual(message.content, "Hello World")

    def test_chatmessage_str(self):
        message = ChatMessage.objects.get(content="Hello World")
        self.assertEqual(str(message), "Hello World")

    def test_chatmessage_link_to_room_and_user(self):
        message = ChatMessage.objects.get(content="Hello World")
        self.assertEqual(message.user.username, "testuser")
        self.assertEqual(message.room.name, "Test Room")
