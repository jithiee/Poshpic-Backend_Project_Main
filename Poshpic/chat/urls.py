from django.urls import path,include
from .views import MessageList , ListUser, ChatHistoryView , DeleteMessageView , ChatNotification
from .routing import websocket_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path("ws/", include(websocket_urlpatterns)),
    path("chat/", ListUser.as_view()),
    path('messages/',MessageList.as_view()),
    path("messages/<int:message_id>/", MessageList.as_view()),
    path("chat_history/<str:room_name>/", ChatHistoryView.as_view()),
    path("delete_message/<int:message_id>/",DeleteMessageView.as_view()),
    path("proroom/", ChatNotification.as_view()),
 
]
    
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
    

    

