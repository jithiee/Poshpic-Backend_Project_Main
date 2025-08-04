from django.contrib import admin
from booking.models import BookingPhotographer

# Register your models here.


@admin.register(BookingPhotographer)
class BookingPhotographerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "photographer",
        "booking_date",
        "booking_status",
        "is_completed",
    ]
