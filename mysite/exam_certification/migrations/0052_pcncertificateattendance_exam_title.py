# Generated by Django 4.0.6 on 2022-08-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0051_alter_exammaterialpautl2_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcncertificateattendance',
            name='exam_title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
