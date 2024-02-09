from django.contrib.auth.models import User
from django.urls import re_path
from chatroom.consumers import ChatConsumer
from chatroom.models import ChatRoom
from channels.routing import URLRouter
from channels.testing import WebsocketCommunicator, ChannelsLiveServerTestCase


class ChatConsumerTest(ChannelsLiveServerTestCase):
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
        # Path to your consumer
        communicator = WebsocketCommunicator(
            application=self.application, path=f"/ws/chat/{self.room_id}/"
        )
        # Force authentication
        communicator.scope["user"] = self.user

        # Connect to the WebSocket
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)

        # Prepare a message
        message = {"message": "Hello, world!"}
        await communicator.send_json_to(message)

        # Receive and assert the response
        response = await communicator.receive_json_from()
        self.assertEqual(response["message"], "Hello, world!")
        self.assertEqual(response["username"], self.user.username)
        # You might need to adjust the timestamp format based on how it's implemented in your consumer
        # self.assertEqual(response["timestamp"], expected_timestamp)

        # Clean up
        await communicator.disconnect()

    async def tearDown(self):
        await self.user.delete()
        await self.room.delete()
