# Generated by Django 4.0.4 on 2022-05-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0039_rename_general_theory_exam_result_phasedarrayultrasonictesting_paut_level2pcn_specific_theory'),
    ]

    operations = [
        migrations.AddField(
            model_name='cswipweldinginspector3_1result',
            name='invigilator',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]