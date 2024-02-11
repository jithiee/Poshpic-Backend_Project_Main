import json
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer
from booking.models import BookingPhotographer
from .models import Message
from datetime import datetime
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from booking.models import BookingPhotographer
from .models import Message

class TextRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    @database_sync_to_async
    def create_message(self, message, sender, room_name):
        try:
            booking = BookingPhotographer.objects.get(id=int(room_name))
            message_obj = Message.objects.create(
                room_name=booking,
                username=sender,
                message=message,
            )
            print(message_obj,'msssssssssssssssssss')
            
            return message_obj
        except BookingPhotographer.DoesNotExist:
            return None
        except ValueError:
            return None 
        except Exception as e:
            print(f'Error creating message: {e}')

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json['message']  # Use 'message' instead of 'text'
        sender = text_data_json['username']

        await self.create_message(text, sender, self.room_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text,
                'sender': sender,
                'timestamp': str(datetime.now()),
                
            }   
        )


    async def chat_message(self, event):
        message = event['message']
        username = event['sender']
        timestamp = event['timestamp']  

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'timestamp': timestamp,
        }))


