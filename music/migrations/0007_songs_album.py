# Generated by Django 3.0.8 on 2020-07-12 17:48

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_songs_uploader'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='album',
            field=models.ImageField(null=True, upload_to='album/', verbose_name=django.contrib.auth.models.User),
        ),
    ]