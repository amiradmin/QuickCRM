# Generated by Django 4.0.1 on 2022-04-13 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0041_rename_explanation_cswipweldinginspector3_1exammaterial_remarks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSWIPWeldingInspector3_1ResultIntermadiate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_result_31_intermediate', to='exam_certification.cswipweldinginspector3_1exammaterial')),
                ('previouse_exam', models.ManyToManyField(blank=True, null=True, to='exam_certification.CSWIPWeldingInspector3_1Result')),
            ],
        ),
    ]
