from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView
from account.models import User
from account.serializers import Userserializer
from rest_framework. response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from booking.serializer import BookingSerializer
from booking.models import BookingPhotographer
from django.conf import settings    
from .serializer import PaymentSerilaizer
from .models import Payment
from datetime import datetime
from django.db.models import Q
import stripe
from rest_framework.permissions import IsAuthenticated 
from datetime import timedelta



class UserList(ListAPIView):
    queryset = User.objects.filter(is_user=True)
    serializer_class = Userserializer


class PhotographerList(ListAPIView):
    queryset = User.objects.filter(is_photographer=True)
    serializer_class = Userserializer
    
    
class UsersDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = not instance.is_active
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookingView(ListAPIView):
    queryset = BookingPhotographer.objects.all()
    serializer_class = BookingSerializer    
    
    
class BookingFilterApivew(APIView):
    @swagger_auto_schema(
        tags=["Booking details"],
        operation_description="Booking details",
        responses={200: BookingSerializer, 400: "bad request", 500: "errors"},
    )        
    
    def get(self, request, action):
        bookings = BookingPhotographer.objects.filter(status=action)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookingDetails(APIView):
    @swagger_auto_schema(
        tags=["Booking details"],
        operation_description="Booking details",
        responses={200: BookingSerializer, 400: "bad request", 500: "errors"},
    )
    def get(self, request, pk):
        try:
            booking = BookingPhotographer.objects.filter(id=pk).first()
        except BookingPhotographer.DoesNotExist:
            return Response({"detail": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
stripe.api_key = settings.STRIPE_SECRET_KEY

class AdminPayment(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            payment = Payment.objects.get(
                Q(Photogarpher=request.user),
                Q(month=datetime.now().month, year=datetime.now().year),
            )

        except Payment.DoesNotExist:
            return Response({"detail": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PaymentSerilaizer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        product = stripe.Product.create(name="Subscription", type="service")

        price = stripe.Price.create(
            unit_amount=int(2500),
            product=product.id,
            currency="usd",
        )

        customer = stripe.Customer.create(
            email=request.user.email , name=request.user.username
        )

        try:               

            success_url = f"http://localhost:3000/success/?success=true&session_id={{CHECKOUT_SESSION_ID}}"
            cancel_url = "http://127.0.0.1:8000/?canceled=true"
            
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price": price.id,
                        "quantity": 1,
                    },
                ],
                mode="payment",
                customer=customer.id,
                success_url=success_url,
                cancel_url=cancel_url,
            )
            if checkout_session.id:
                expiration_date = datetime.now() + timedelta(days=365)
                
                Payment.objects.create(
                    Photogarpher=request.user,
                month=datetime.now().month,
                year=datetime.now().year,
                stripe_id =checkout_session.id,
                amount=2500,total_amount=2500,
                expiration_date=expiration_date
                
                
                
                )
                        
            return Response({"url": checkout_session.url}, status=status.HTTP_200_OK)

        except stripe.error.StripeError as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class PaymentSuccessView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session_id = request.data.get("session_id")
        payment = Payment.objects.get(stripe_id=session_id)
        payment.status = "completed"
        payment.save()
        user = payment.Photogarpher
        user.is_blocked = False
        user.save()
        return Response({"msg": "Completed Successfully"}, status=status.HTTP_200_OK)
    
    
class PhotographerPayment(APIView):
    permission_classes = [IsAuthenticated ]
    def get(self, request):
        try:
            payment = Payment.objects.all()
            serializer = PaymentSerilaizer(payment, many=True)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({"error":"Not payment is found"},status=status.HTTP_404_NOT_FOUND)
        


    
    
    




    
    
    

