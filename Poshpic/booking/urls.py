from django.urls import path
from . import views


urlpatterns = [
    path("booking/<int:pk>/", views.BookingApiView.as_view()),

    
    
]
