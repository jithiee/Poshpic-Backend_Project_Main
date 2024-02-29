from rest_framework import serializers
from .models import BookingPhotographer
import datetime


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingPhotographer
        fields = [
            "user",
            "photographer",
            "booking_date",
            "booking_status",
            "is_completed",
        ]

