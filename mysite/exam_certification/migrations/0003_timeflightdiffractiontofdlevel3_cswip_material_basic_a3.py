# Generated by Django 4.0.1 on 2022-04-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0002_bgas_cswip_paintinginspectormaterial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeflightdiffractiontofdlevel3_cswip_material',
            name='basic_a3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
