# Generated by Django 4.0.1 on 2022-04-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0069_digitalradiographicinterpretationdri_level2_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammaterialphasedarrayultrasonictesting_paut_level2cswip',
            name='general_theory',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammaterialphasedarrayultrasonictesting_paut_level2cswip',
            name='specific_theory',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
