# Generated by Django 5.0.2 on 2024-03-03 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_alter_bookingphotographer_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookingphotographer",
            name="booking_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 3, 18, 28, 53, 46376)
            ),
        ),
    ]
