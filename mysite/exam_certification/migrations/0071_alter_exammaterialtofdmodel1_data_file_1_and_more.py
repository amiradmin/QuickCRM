# Generated by Django 4.0.1 on 2022-04-19 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0070_alter_exammaterialphasedarrayultrasonictesting_paut_level2cswip_general_theory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammaterialtofdmodel1',
            name='data_file_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pautl2_data1', to='exam_certification.samples'),
        ),
        migrations.AlterField(
            model_name='exammaterialtofdmodel1',
            name='data_file_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pautl2_data2', to='exam_certification.samples'),
        ),
        migrations.AlterField(
            model_name='exammaterialtofdmodel1',
            name='data_file_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pautl2_data3', to='exam_certification.samples'),
        ),
        migrations.AlterField(
            model_name='exammaterialtofdmodel1',
            name='data_file_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pautl2_data4', to='exam_certification.samples'),
        ),
        migrations.AlterField(
            model_name='exammaterialtofdmodel1',
            name='data_file_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pautl2_data5', to='exam_certification.samples'),
        ),
        migrations.AlterField(
            model_name='exammaterialtofdmodel1',
            name='sample1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pautl2_sample1', to='exam_certification.samples'),
        ),
        migrations.AlterField(
            model_name='exammaterialtofdmodel1',
            name='sample2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pautl2_sample2', to='exam_certification.samples'),
        ),
    ]
