# Generated by Django 4.0.1 on 2022-03-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0069_tescandidate_disable_timesheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='exam_att_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='traning_att_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
