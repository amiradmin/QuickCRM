# Generated by Django 4.0.1 on 2022-02-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0060_event_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='tescandidate',
            name='form_category',
            field=models.ManyToManyField(blank=True, null=True, to='training.Category'),
        ),
    ]
