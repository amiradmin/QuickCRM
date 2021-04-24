# Generated by Django 3.2 on 2021-04-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0014_alter_event_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='announcement_type',
            field=models.CharField(blank=True, choices=[('S', 'SMS'), ('E', 'Email')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
