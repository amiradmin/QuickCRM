# Generated by Django 3.2.5 on 2021-10-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20211030_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='TicketNumber',
            field=models.CharField(blank=True, default='TESTIK-0', max_length=256, null=True),
        ),
    ]
