# Generated by Django 3.2.4 on 2021-06-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0028_remove_candidateprofile_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='training.Skill'),
        ),
    ]
