# Generated by Django 4.1.7 on 2024-01-10 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0008_alter_bike_bike_name_alter_bike_image_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikemeta',
            name='latest_upload',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 18, 27, 51, 665317)),
        ),
    ]
