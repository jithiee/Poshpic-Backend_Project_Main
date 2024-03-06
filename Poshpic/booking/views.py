from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User
from .serializer import BookingSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import BookingPhotographer 
from datetime import datetime
from account.models import PhotographerProfile


class BookingApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        photographer = User.objects.get(id=pk)
        data = {
          "photographer": photographer.id,
           "user": request.user.id,
             **(request.data if isinstance(request.data, dict) else {}),  # str to dict
              # "booking_date": request.data.get("booking_date"),
                # "amount": request.data.get("amount") 
        }
        
        booking_date_str = data.get("booking_date")
        print(booking_date_str,'22222')
        
        if booking_date_str:
            try:
        
                booking_date = datetime.strptime(booking_date_str, '%Y-%m-%dT%H:%M')
             

            except ValueError:
                return Response({'msg': 'Invalid booking date format'}, status=status.HTTP_400_BAD_REQUEST)

            if booking_date <= datetime.now():
                return Response({'msg': 'Booking date must be a future date'}, status=status.HTTP_400_BAD_REQUEST)
            

        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
        
            serializer.save()
            print(serializer.data,'555555')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )
    
        
    def get(self , request ):
        try:
            bookings = BookingPhotographer.objects.filter(user = request.user ).order_by("-booking_date") 
            serializer = BookingSerializer(bookings , many = True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        except BookingPhotographer.DoesNotExist:
            return Response({'msg':'booking not found'} , status=status.HTTP_404_NOT_FOUND)
        
        
        
        
        
        
          


















































# def get(self, request, pk):
#     try:
#         if pk is not None:
#             bookinguser = BookingPhotographer.objects.get(pk=pk)
#             serializer = BookingSerializer(bookinguser)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             booking_users = BookingPhotographer.objects.all()
#             serializer = BookingSerializer(booking_users, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#     except BookingPhotographer.DoesNotExist:
#         return Response({"detail": "Photographer not found"}, status=status.HTTP_404_NOT_FOUND)
