# Generated by Django 3.2.5 on 2021-10-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_alter_ticket_asignedto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketanswer',
            name='asignedTo',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
