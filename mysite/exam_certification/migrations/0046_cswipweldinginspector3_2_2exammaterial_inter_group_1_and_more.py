# Generated by Django 4.0.4 on 2022-05-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0045_cswipweldinginspector3_2_2exammaterial_plant_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='cswipweldinginspector3_2_2exammaterial',
            name='inter_group_1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cswipweldinginspector3_2_2exammaterial',
            name='inter_group_2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cswipweldinginspector3_2_2exammaterial',
            name='inter_group_3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cswipweldinginspector3_2_2exammaterial',
            name='inter_group_4',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
