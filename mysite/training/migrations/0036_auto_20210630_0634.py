# Generated by Django 3.2.4 on 2021-06-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0035_auto_20210630_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='candidates',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='last_name',
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='events',
            field=models.ManyToManyField(to='training.Event'),
        ),
        migrations.DeleteModel(
            name='CandidateProfileOne',
        ),
    ]
