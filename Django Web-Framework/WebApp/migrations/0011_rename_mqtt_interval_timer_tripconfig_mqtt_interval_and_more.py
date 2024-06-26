# Generated by Django 5.0.3 on 2024-04-20 12:10

import WebApp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0010_remove_trip_data_logger_config_trip_psd_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tripconfig',
            old_name='mqtt_interval_timer',
            new_name='mqtt_interval',
        ),
        migrations.RenameField(
            model_name='tripconfig',
            old_name='vibration_interval_timer',
            new_name='vibration_sampling_interval',
        ),
        migrations.RenameField(
            model_name='tripconfig',
            old_name='vibration_magnitude_threshold',
            new_name='vibration_threshold',
        ),
        migrations.RemoveField(
            model_name='tripconfig',
            name='bme_interval_timer',
        ),
        migrations.RemoveField(
            model_name='tripconfig',
            name='interval_bme_recording',
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='bme_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='bme_sampling_duration',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='bme_sampling_interval',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='esp_stats_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='gps_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='impact_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='logs_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='movement_detection_threshold',
            field=models.FloatField(default=0.3),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='mqtt_address',
            field=models.CharField(default='172.187.90.157', max_length=255),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='mqtt_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='mqtt_port',
            field=models.IntegerField(default=1883, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)]),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='sleep_interval',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='sleep_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tripconfig',
            name='vibration_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trip',
            name='bme_data',
            field=models.FileField(blank=True, null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AlterField(
            model_name='trip',
            name='gps_data',
            field=models.FileField(blank=True, null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AlterField(
            model_name='trip',
            name='impact_data',
            field=models.FileField(blank=True, null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AlterField(
            model_name='trip',
            name='psd_data',
            field=models.FileField(blank=True, null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
        migrations.AlterField(
            model_name='trip',
            name='vibration_data',
            field=models.FileField(blank=True, null=True, upload_to=WebApp.models.Trip.get_upload_path),
        ),
    ]
