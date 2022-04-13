# Generated by Django 4.0.1 on 2022-04-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0038_cswipweldinginspector3_1exammaterial_exam_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cswipweldinginspector3_1exammaterial',
            name='customerID',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cswipweldinginspector3_1exammaterial',
            name='exam_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cswipweldinginspector3_1exammaterial',
            name='invigilator',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cswipweldinginspector3_1exammaterial',
            name='lecturer',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]