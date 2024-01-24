from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import re_path
from chatroom.consumers import ChatConsumer
from chatroom.models import ChatRoom
from channels.routing import URLRouter
from channels.testing import WebsocketCommunicator


class ChatConsumerTest(TestCase):
    """
    This class is to test `chatroom.consumers` module.
    """

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
