import json
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer
from booking.models import BookingPhotographer
from .models import Message,Room
from datetime import datetime
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from booking.models import BookingPhotographer
from .models import Message


class TextRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def create_message(self, message, username, room_name):
        room = Room.objects.get_or_create(name=room_name)[0]
        message_obj = Message.objects.create(
            message=message,
            username=username,
            room=room,
            )
        return message_obj

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        room_name = self.room_name

        message_obj = await self.create_message(message, username, room_name)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message_obj.message,
                "username": message_obj.username,
                "timestamp": str(message_obj.timestamp),
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        timestamp = event["timestamp"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "timestamp": timestamp,
                }
            )
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # async def connect(self):
    #     self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
    #     print('chattttttttttttt')
    #     self.room_group_name = f"chat_{self.room_name}"

    #     await self.channel_layer.group_add(self.room_group_name, self.channel_name)
    #     await self.accept()

    # async def disconnect(self, close_code):
    #     await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # @database_sync_to_async
    # def create_message(self, messge, sender, room_name):       
    #     try:
    #         booking = BookingPhotographer.objects.get(id=int(room_name))

    #         message_obj = Message.objects.create(
    #             room_name=booking,
    #             username=sender,
    #             message=message,
    #         )
    #         print(message_obj, "msssssssssssssssssss")

    #         return message_obj
    #     except BookingPhotographer.DoesNotExist:
    #         return None
    #     except ValueError:
    #         return None
    #     except Exception as e:
    #         print(f"Error creating message: {e}")

    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     text = text_data_json["message"]
    #     sender = text_data_json["username"]

    #     await self.create_message(text, sender, self.room_name)

    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             "type": "chat_message",
    #             "message": text,
    #             "sender": sender,
    #             "timestamp": str(datetime.now()),
    #         },
    #     )

    # async def chat_message(self, event):
    #     message = event["message"]
    #     username = event["sender"]
    #     timestamp = event["timestamp"]

    #     await self.send(
    #         text_data=json.dumps(
    #             {
    #                 "message": message,
    #                 "username": username,
    #                 "timestamp": timestamp,
    #             }
    #         )
    #     )
