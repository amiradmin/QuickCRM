# Generated by Django 3.1.6 on 2021-04-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='passport_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
