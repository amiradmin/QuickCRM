# Generated by Django 3.2.5 on 2021-10-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20211019_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='archived',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='readFlag',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
