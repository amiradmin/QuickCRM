# Generated by Django 3.2.4 on 2021-07-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0017_general_confirmation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='general',
            name='confirmation',
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='confirmation',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='eventID',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
