# Generated by Django 4.0.1 on 2022-01-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0001_initial'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='timesheet',
        #     name='from_date',
        #     field=models.DateTimeField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='timesheet',
        #     name='to_date',
        #     field=models.DateTimeField(blank=True, null=True),
        # ),
        migrations.AlterField(
            model_name='timesheet',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
