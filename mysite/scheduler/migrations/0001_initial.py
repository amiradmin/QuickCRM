# Generated by Django 4.0.1 on 2022-03-15 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stafftimesheet', '0006_timesheet_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimesheetChecker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger', models.BooleanField(blank=True, default=False, null=True)),
                ('timesheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timesheet_scheduler', to='stafftimesheet.timesheet')),
            ],
        ),
    ]
