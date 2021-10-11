# Generated by Django 3.2.5 on 2021-10-04 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0040_alter_event_formcategory'),
        ('forms', '0053_auto_20211003_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesAttCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testSequence', models.CharField(blank=True, max_length=1024, null=True)),
                ('dayOneSec1', models.BooleanField(blank=True, null=True)),
                ('dayOneSec2', models.BooleanField(blank=True, null=True)),
                ('dayOneSec3', models.BooleanField(blank=True, null=True)),
                ('dayOneSec4', models.BooleanField(blank=True, null=True)),
                ('dayOneSec5', models.BooleanField(blank=True, null=True)),
                ('dayTwoSec1', models.BooleanField(blank=True, null=True)),
                ('dayTwoSec2', models.BooleanField(blank=True, null=True)),
                ('dayTwoSec3', models.BooleanField(blank=True, null=True)),
                ('dayTwoSec4', models.BooleanField(blank=True, null=True)),
                ('dayTwoSec5', models.BooleanField(blank=True, null=True)),
                ('dayThreeSec1', models.BooleanField(blank=True, null=True)),
                ('dayThreeSec2', models.BooleanField(blank=True, null=True)),
                ('dayThreeSec3', models.BooleanField(blank=True, null=True)),
                ('dayThreeSec4', models.BooleanField(blank=True, null=True)),
                ('dayThreeSec5', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tes_att_candidate', to='training.tescandidate')),
            ],
        ),
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
        migrations.CreateModel(
            name='TrainingAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examTitleCode', models.CharField(blank=True, max_length=2048, null=True)),
                ('venue', models.CharField(blank=True, max_length=2048, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('lecturerName', models.CharField(blank=True, max_length=2048, null=True)),
                ('confirmation', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attCandidate', models.ManyToManyField(blank=True, null=True, to='forms.TesAttCandidate')),
            ],
        ),
    ]