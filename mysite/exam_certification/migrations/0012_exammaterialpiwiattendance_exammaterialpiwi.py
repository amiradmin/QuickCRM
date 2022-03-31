# Generated by Django 4.0.1 on 2022-03-31 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0070_event_exam_att_file_event_traning_att_file'),
        ('exam_certification', '0011_cswipcertificateattendance_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamMaterialPiWiAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('exam_date', models.DateTimeField(blank=True, null=True)),
                ('exam_revision', models.CharField(blank=True, max_length=256, null=True)),
                ('lecturer', models.CharField(blank=True, max_length=256, null=True)),
                ('invigilator', models.CharField(blank=True, max_length=256, null=True)),
                ('remark', models.CharField(blank=True, max_length=2048, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='exam_file')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pi_candidate', to='training.tescandidate')),
            ],
        ),
        migrations.CreateModel(
            name='ExamMaterialPiWi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='exam_file')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendance', models.ManyToManyField(blank=True, null=True, to='exam_certification.ExamMaterialPiWiAttendance')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_material_pi_event', to='training.event')),
            ],
        ),
    ]
