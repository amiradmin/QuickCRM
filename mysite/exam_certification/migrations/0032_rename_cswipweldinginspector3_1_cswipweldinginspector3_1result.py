# Generated by Django 4.0.1 on 2022-04-12 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0071_event_end_exam_date_event_start_exam_date'),
        ('exam_certification', '0031_cswipweldinginspector3_1exammaterial_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CSWIPWeldingInspector3_1',
            new_name='CSWIPWeldingInspector3_1Result',
        ),
    ]