# Generated by Django 4.0.6 on 2022-08-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0053_remove_pcncertificateattendance_exam_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificateattendance',
            name='exam_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
