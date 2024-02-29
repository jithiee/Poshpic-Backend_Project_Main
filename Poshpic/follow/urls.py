from django.urls import path
from . import views


urlpatterns = [
    path("follow/<int:pk>/", views.FollowApiView.as_view()),
    
]
