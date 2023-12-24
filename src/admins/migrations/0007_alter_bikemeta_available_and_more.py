# Generated by Django 4.2.8 on 2023-12-24 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0006_alter_bike_image_name_alter_bikeimages_image_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikemeta',
            name='available',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bikemeta',
            name='latest_upload',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 19, 42, 40, 242316)),
        ),
        migrations.AlterField(
            model_name='bikemeta',
            name='no_of_owners',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
