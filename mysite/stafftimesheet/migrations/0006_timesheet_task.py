# Generated by Django 4.0.1 on 2022-03-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stafftimesheet', '0005_alter_timesheet_from_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='task',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]