# Generated by Django 4.0.4 on 2022-05-24 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0074_alter_tescandidate_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateprofile',
            name='user',
        ),
    ]
