# Generated by Django 5.0.2 on 2024-03-03 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("follow", "0002_alter_follow_create_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="create_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 3, 18, 28, 52, 998852)
            ),
        ),
    ]
