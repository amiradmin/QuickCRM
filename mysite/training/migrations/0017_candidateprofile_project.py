# Generated by Django 3.2.4 on 2021-06-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0016_auto_20210620_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='project',
            field=models.ManyToManyField(blank=True, null=True, to='training.CandidateProject'),
        ),
    ]
