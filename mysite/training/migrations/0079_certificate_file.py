# Generated by Django 4.0.4 on 2022-06-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0078_event_deliverymethod'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
    ]