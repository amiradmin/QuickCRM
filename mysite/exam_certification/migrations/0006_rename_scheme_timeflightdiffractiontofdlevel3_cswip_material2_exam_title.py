# Generated by Django 4.0.1 on 2022-04-21 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0005_timeflightdiffractiontofdlevel3_cswip_material2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeflightdiffractiontofdlevel3_cswip_material2',
            old_name='scheme',
            new_name='exam_title',
        ),
    ]
