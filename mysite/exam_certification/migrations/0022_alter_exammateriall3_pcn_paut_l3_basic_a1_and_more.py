# Generated by Django 4.0.1 on 2022-04-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0021_alter_exammateriall3_paut_basic_a1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_basic_a1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_basic_a2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_basic_b_part_1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_basic_b_part_2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_basic_b_part_3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_basic_b_part_4',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_delivery_method',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_main_d',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_main_e',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_main_f',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_ndtl3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_pautl2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_paut_l3_practical_exam',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_basic_a1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_basic_a2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_basic_b_part_1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_basic_b_part_2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_basic_b_part_3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_basic_b_part_4',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_delivery_method',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_main_d',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_main_e',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_main_f',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_ndtl3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_pautl2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='pcn_tofd_l3_practical_exam',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_basic_a1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_basic_a2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_basic_b_part_1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_basic_b_part_2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_basic_b_part_3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_basic_b_part_4',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_delivery_method',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_main_c_1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_main_c_2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_main_c_3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_ndtl3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_pautl2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='exammateriall3',
            name='tofd_practical_exam',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
