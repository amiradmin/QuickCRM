# Generated by Django 4.0.1 on 2022-04-14 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0048_cswipweldinginspector3_1resultintermadiate_result_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cswipweldinginspector3_1resultintermadiate',
            old_name='result',
            new_name='primary',
        ),
        migrations.RenameField(
            model_name='cswipweldinginspector3_1resultintermadiate',
            old_name='result_1',
            new_name='secondry',
        ),
        migrations.RemoveField(
            model_name='cswipweldinginspector3_1resultintermadiate',
            name='result_2',
        ),
    ]
