from django.urls import path

from adminpanel.views import BookingDetails  
from adminpanel.views import (
    UserList,
    PhotographerList,
    UsersDetailsView,
    BookingView,AdminPayment,PaymentSuccessView

    
)

urlpatterns = [
    path("userslist/", UserList.as_view(), name="user-list"),
    path("photographerlist/", PhotographerList.as_view(), name="user-list"),
    path("details_view/<int:pk>/", UsersDetailsView.as_view(), name="user-list"),
    path("booking_list/", BookingView.as_view(), name="user-list"),
    path("payment/", AdminPayment.as_view(), name="payment"),
    path("success/", PaymentSuccessView.as_view(), name="success"),
    
]
    
    
