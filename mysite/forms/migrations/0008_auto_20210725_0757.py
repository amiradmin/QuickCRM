# Generated by Django 3.2.4 on 2021-07-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20210724_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='twienrolmentform',
            name='NDTexamination',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='NDTexaminationCategories',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='NDTexaminationLevel',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='PCN_BGASApprovalNumber',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='VerifierCompanyPosition',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='VerifierDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='VerifierEmail',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='VerifierName',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='VerifierProfessionalRelation',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='VerifierTelephone',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='currentCSWIPQualifications',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='examination',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='experience',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='experienceRequirements',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='otherExaminations',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='plantInspection',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='plantInspectionLevel',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='plantInspectionRequirements',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AddField(
            model_name='twienrolmentform',
            name='underwaterInspectionExam',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
