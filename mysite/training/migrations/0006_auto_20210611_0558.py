# Generated by Django 3.2.4 on 2021-06-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_lecturer_document_10'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='log',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
