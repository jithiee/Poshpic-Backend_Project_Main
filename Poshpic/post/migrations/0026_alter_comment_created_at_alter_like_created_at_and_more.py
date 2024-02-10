# Generated by Django 5.0 on 2024-01-22 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_alter_comment_created_at_alter_like_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 53, 15, 371142)),
        ),
        migrations.AlterField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 53, 15, 371142)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 53, 15, 371142)),
        ),
        migrations.AlterField(
            model_name='posthistory',
            name='deleted_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 53, 15, 371142)),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 53, 15, 372138)),
        ),
    ]
