# from channels.routing import ProtocolTypeRouter, URLRouter
# # import app.routing
# from django.urls import re_path
# from .consumers import TextRoomConsumer
# websocket_urlpatterns = [
#     re_path(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),
# ]

# application = ProtocolTypeRouter({
#     'websocket':
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ,
# })
from django.urls import re_path
from .consumers import TextRoomConsumer

websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),
]

# asgi.py (for channels)
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(websocket_urlpatterns),
    }
)

