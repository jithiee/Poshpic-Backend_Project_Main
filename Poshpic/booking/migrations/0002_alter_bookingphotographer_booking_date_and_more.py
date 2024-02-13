# Generated by Django 5.0 on 2024-01-22 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookingphotographer",
            name="booking_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 22, 15, 5, 52, 601707)
            ),
        ),
        migrations.AlterField(
            model_name="bookingphotographer",
            name="booking_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("completed", "Completed"),
                ],
                default="pending",
                max_length=50,
            ),
        ),
    ]
