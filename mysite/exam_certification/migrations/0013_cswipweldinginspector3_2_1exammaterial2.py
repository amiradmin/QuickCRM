# Generated by Django 4.0.1 on 2022-04-21 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0071_event_end_exam_date_event_start_exam_date'),
        ('exam_certification', '0012_alter_cswipweldinginspector3_2_1exammaterial_general_theory_s_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSWIPWeldingInspector3_2_1ExamMaterial2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('result', models.CharField(blank=True, max_length=128, null=True)),
                ('exam_date', models.DateTimeField(blank=True, null=True)),
                ('scheme', models.CharField(blank=True, max_length=256, null=True)),
                ('exam_title', models.CharField(blank=True, max_length=256, null=True)),
                ('customerID', models.CharField(blank=True, max_length=256, null=True)),
                ('lecturer', models.CharField(blank=True, max_length=256, null=True)),
                ('invigilator', models.CharField(blank=True, max_length=256, null=True)),
                ('remarks', models.CharField(blank=True, max_length=4096, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='exam_result_file')),
                ('general_theory_s', models.CharField(blank=True, max_length=256, null=True)),
                ('ndt_s', models.CharField(blank=True, max_length=256, null=True)),
                ('symbols_s', models.CharField(blank=True, max_length=256, null=True)),
                ('scenario_s', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_result_candidate_321_exam_material2', to='training.tescandidate')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_result_event_321_exam_material2', to='training.event')),
            ],
        ),
    ]
