# Generated by Django 4.0.4 on 2022-05-31 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0049_cswipweldinginspector3_1result_overall'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgas_cswip_paintinginspectorresult',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cswipweldinginspector3_2_1_result',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cswipweldinginspector3_2_2_result',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='digitalradiographicinterpretationdri_level2_result',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='exam_result_phasedarrayultrasonictesting_paut_level2cswip',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='exam_result_phasedarrayultrasonictesting_paut_level2pcn',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='exam_result_phasedarrayultrasonictesting_tofd_level2pcn',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='exammaterialtofd_cswip',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='phasedarrayultrasonictesting_paut_l3_pcn_result',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='phasedarrayultrasonictesting_paut_l3cswipresult',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='radiographicinterpretationweldsriresult',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='timeflightdiffractiontofdlevel3_cswip_result',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='timeflightdiffractiontofdlevel3_pcn_result3',
            name='overall',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
