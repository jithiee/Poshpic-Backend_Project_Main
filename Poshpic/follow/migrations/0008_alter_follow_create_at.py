# Generated by Django 5.0 on 2024-01-22 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0007_alter_follow_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 5, 52, 571852)),
        ),
    ]
