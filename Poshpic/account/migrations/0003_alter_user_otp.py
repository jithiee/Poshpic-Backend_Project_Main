# Generated by Django 5.0.2 on 2024-11-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_user_otp_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="otp",
            field=models.IntegerField(max_length=4, null=True),
        ),
    ]
