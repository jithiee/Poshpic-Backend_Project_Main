# Generated by Django 5.0.2 on 2024-11-20 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("follow", "0003_alter_follow_create_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="create_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 11, 20, 10, 59, 51, 172857)
            ),
        ),
    ]
