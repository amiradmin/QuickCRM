# Generated by Django 4.0.4 on 2022-05-14 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0038_alter_exammaterialphasedarrayultrasonictesting_tofd_level2pcn_sample1_analysis_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_result_phasedarrayultrasonictesting_paut_level2pcn',
            old_name='general_theory',
            new_name='specific_theory',
        ),
    ]
