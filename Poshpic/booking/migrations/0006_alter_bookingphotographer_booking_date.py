# Generated by Django 5.0 on 2024-02-10 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_bookingphotographer_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingphotographer',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 16, 15, 31, 829031)),
        ),
    ]
