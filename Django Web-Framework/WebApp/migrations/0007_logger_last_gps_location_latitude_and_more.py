# Generated by Django 5.0.3 on 2024-04-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_logger_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='last_gps_location_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='logger',
            name='last_gps_location_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
