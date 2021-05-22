# Generated by Django 3.2 on 2021-05-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0023_auto_20210516_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='user',
        ),
        migrations.AddField(
            model_name='lecturer',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
