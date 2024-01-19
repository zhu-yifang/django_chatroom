import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chatroom.models import ChatRoom, ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Since we have many rooms, we need to create a group for each room
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Save the message to the database
        await self.save_message(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @database_sync_to_async
    def save_message(self, message):
        # Assuming 'user' and 'room' are available in the scope
        user = self.scope["user"]
        room_id = self.scope["url_route"]["kwargs"]["room_id"]
        room = ChatRoom.objects.get(id=room_id)

        ChatMessage.objects.create(user=user, room=room, content=message)
