# Generated by Django 5.0 on 2024-01-16 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_post_created_at_alter_posthistory_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 23, 13, 38, 488532)),
        ),
        migrations.AlterField(
            model_name='posthistory',
            name='deleted_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 23, 13, 38, 489526)),
        ),
        migrations.AlterField(
            model_name='posthistory',
            name='post',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
