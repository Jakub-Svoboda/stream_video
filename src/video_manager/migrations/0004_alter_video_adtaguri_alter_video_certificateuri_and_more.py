# Generated by Django 4.2.3 on 2023-08-27 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0003_alter_video_clearkeys_alter_video_drm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='adTagUri',
            field=models.URLField(blank=True, max_length=2000, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='video',
            name='certificateUri',
            field=models.URLField(blank=True, max_length=2000, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='video',
            name='iconUri',
            field=models.URLField(max_length=2000, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='video',
            name='manifestUri',
            field=models.URLField(max_length=2000, validators=[django.core.validators.URLValidator()]),
        ),
    ]
