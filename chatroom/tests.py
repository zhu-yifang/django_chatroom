# FILEPATH: /Users/zhuyifang/workspace/django_chatroom/chatroom/tests.py
from django.test import TestCase, Client
from django.urls import re_path, reverse
from django.contrib.auth.models import User

from chatroom.consumers import ChatConsumer
from .models import ChatRoom, ChatMessage
from channels.routing import URLRouter
from channels.testing import WebsocketCommunicator


class ChatRoomViewTest(TestCase):
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


class ChatConsumerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")

        # Create a ChatRoom instance
        self.room = ChatRoom.objects.create(name="Test Room")
        self.room_id = self.room.id  # Use the ID of the created room

        self.application = URLRouter(
            [
                re_path(r"ws/chat/(?P<room_id>\w+)/$", ChatConsumer.as_asgi()),
            ]
        )

    async def test_chat_consumer(self):
        communicator = WebsocketCommunicator(
            self.application, f"/ws/chat/{self.room_id}/"
        )
        communicator.scope["user"] = self.user
        connected, _ = await communicator.connect()
        assert connected

        message = "Hello, world!"
        await communicator.send_json_to({"message": message})

        response = await communicator.receive_json_from()
        assert response["message"] == message
        assert response["username"] == self.user.username

        await communicator.disconnect()

    def tearDown(self):
        self.user.delete()
