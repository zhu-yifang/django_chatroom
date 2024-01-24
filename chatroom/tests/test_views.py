# FILEPATH: /Users/zhuyifang/workspace/django_chatroom/chatroom/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import ChatRoom, ChatMessage


class ChatRoomViewTest(TestCase):
    """
    This class is to test `chatroom.views` module.
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.room = ChatRoom.objects.create(name="Test Room")
        self.message1 = ChatMessage.objects.create(
            room=self.room, user=self.user, content="Hello"
        )
        self.message2 = ChatMessage.objects.create(
            room=self.room, user=self.user, content="World"
        )

    def test_chat_room_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("chat_room", args=[self.room.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "chatroom/chat_room.html")
        self.assertContains(response, "Hello")
        self.assertContains(response, "World")

    def test_chat_room_view_no_room(self):
        response = self.client.get(reverse("chat_room", args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_chat_room_list_view(self):
        response = self.client.get(reverse("chat_room_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "chatroom/chat_room_list.html")
        self.assertContains(response, "Test Room")

    def test_chat_room_view(self):
        response = self.client.get(reverse("chat_room", args=[self.room.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "chatroom/chat_room.html")
        self.assertContains(response, "Hello")

    def test_create_room_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.post(reverse("create_room"), {"name": "New Room"})
        self.assertRedirects(response, reverse("chat_room_list"))
        self.assertTrue(ChatRoom.objects.filter(name="New Room").exists())

    def tearDown(self):
        self.room.delete()
        self.user.delete()
