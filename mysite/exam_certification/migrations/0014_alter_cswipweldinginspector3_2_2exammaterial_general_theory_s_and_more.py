# Generated by Django 4.0.1 on 2022-04-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0013_cswipweldinginspector3_2_1exammaterial2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cswipweldinginspector3_2_2exammaterial',
            name='general_theory_s',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='cswipweldinginspector3_2_2exammaterial',
            name='ndt_s',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='cswipweldinginspector3_2_2exammaterial',
            name='scenario_s',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='cswipweldinginspector3_2_2exammaterial',
            name='symbols_s',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
