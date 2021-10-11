# Generated by Django 3.2.5 on 2021-10-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0040_alter_event_formcategory'),
        ('forms', '0050_auto_20210923_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesFrmCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testSequence', models.CharField(blank=True, max_length=1024, null=True)),
                ('scheme', models.CharField(blank=True, max_length=1024, null=True)),
                ('methodOfExam', models.CharField(blank=True, max_length=1024, null=True)),
                ('remark', models.CharField(blank=True, max_length=1024, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tes_frm_candidate', to='training.tescandidate')),
            ],
        ),
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
        migrations.CreateModel(
            name='TesFrmExaminationAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examTitleCode', models.CharField(blank=True, max_length=2048, null=True)),
                ('venue', models.CharField(blank=True, max_length=2048, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('invigilatorName', models.CharField(blank=True, max_length=2048, null=True)),
                ('confirmation', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tesFrmCandidate', models.ManyToManyField(blank=True, null=True, to='forms.TesFrmCandidate')),
            ],
        ),
    ]