# Generated by Django 4.0.1 on 2022-03-15 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheetchecker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 3, 15, 7, 52, 43, 79589)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheetchecker',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]