# Generated by Django 4.0.6 on 2022-08-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0012_alter_ticket_closedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='new_message',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]