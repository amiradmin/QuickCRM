# Generated by Django 4.0.4 on 2022-04-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0018_digitalradiographicinterpretationdri_level2_result_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phasedarrayultrasonictesting_paut_l3_pcn_material',
            name='exam_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
