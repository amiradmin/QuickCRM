# Generated by Django 4.0.4 on 2022-04-24 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0026_alter_cswipweldinginspector3_1result_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cswipweldinginspector3_1result',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam_result_31', to='exam_certification.cswipweldinginspector3_1exammaterial'),
        ),
    ]
