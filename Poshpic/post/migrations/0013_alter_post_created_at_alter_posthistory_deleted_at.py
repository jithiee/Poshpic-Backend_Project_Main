# Generated by Django 5.0 on 2024-01-16 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0012_alter_post_created_at_alter_posthistory_deleted_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 16, 23, 12, 21, 876242)
            ),
        ),
        migrations.AlterField(
            model_name="posthistory",
            name="deleted_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 16, 23, 12, 21, 877227)
            ),
        ),
    ]
