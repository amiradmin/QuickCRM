# Generated by Django 3.2.4 on 2021-07-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_rename_location_forms'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='dbName',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
