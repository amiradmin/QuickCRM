# Generated by Django 3.2.5 on 2021-10-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20211031_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='asignedTo',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]