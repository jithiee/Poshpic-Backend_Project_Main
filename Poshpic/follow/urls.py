from django.urls import path
from  .import views


urlpatterns = [
    path('follow/<int:pk>/',views.FollowApiView.as_view()),
    # path('followers/<int:pk>/',views.PhotographerFollowers.as_view()),
    
]

    
    

