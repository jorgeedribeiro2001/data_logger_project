# Generated by Django 5.0.3 on 2024-04-02 15:25

import WebApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_alter_trip_last_communication_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='bme_data',
            field=models.FileField(null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AddField(
            model_name='trip',
            name='data_logger_config',
            field=models.FileField(null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AddField(
            model_name='trip',
            name='gps_data',
            field=models.FileField(null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AddField(
            model_name='trip',
            name='impact_data',
            field=models.FileField(null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AddField(
            model_name='trip',
            name='vibration_data',
            field=models.FileField(null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AlterField(
            model_name='trip',
            name='log',
            field=models.FileField(null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
    ]
