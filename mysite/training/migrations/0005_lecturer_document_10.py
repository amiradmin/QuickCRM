# Generated by Django 3.2.4 on 2021-06-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_alter_event_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='document_10',
            field=models.FileField(blank=True, null=True, upload_to='lecturer_document'),
        ),
    ]
