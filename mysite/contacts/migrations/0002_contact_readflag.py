# Generated by Django 3.2.5 on 2021-10-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='readFlag',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
