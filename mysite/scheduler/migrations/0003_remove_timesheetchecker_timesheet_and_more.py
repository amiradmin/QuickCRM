# Generated by Django 4.0.1 on 2022-03-23 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_timesheetchecker_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheetchecker',
            name='timesheet',
        ),
        migrations.AddField(
            model_name='timesheetchecker',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 15, 15, 32, 420724)),
            preserve_default=False,
        ),
    ]