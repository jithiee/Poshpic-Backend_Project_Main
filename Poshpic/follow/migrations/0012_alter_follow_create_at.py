# Generated by Django 5.0 on 2024-02-10 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0011_alter_follow_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 16, 15, 31, 808561)),
        ),
    ]
