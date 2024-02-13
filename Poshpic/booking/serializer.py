from rest_framework import serializers
from .models import BookingPhotographer


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingPhotographer
        fields = [
            "user",
            "photographer",
            "booking_date",
            "amount",
            "booking_status",
            "is_completed",
        ]
