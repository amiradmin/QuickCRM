# Generated by Django 3.2.5 on 2021-08-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0022_twienrolmentform_otherexaminationstitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgasexperienceform',
            name='PreCertificationExperience',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='VerifierCompany',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='VerifierDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='VerifierEmail',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='VerifierName',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='VerifierTelephone',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]