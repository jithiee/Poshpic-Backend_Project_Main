# Generated by Django 5.0 on 2024-01-22 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_bookingphotographer_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingphotographer',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 53, 15, 397057)),
        ),
    ]