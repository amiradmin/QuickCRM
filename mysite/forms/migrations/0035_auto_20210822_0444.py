# Generated by Django 3.2.5 on 2021-08-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0034_auto_20210821_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='psl30initialform',
            name='candidateEligibilityDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='candidateEligibilityName',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='examCloseDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='examDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='examinerName',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='examinerVenue',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='expVerifierDetails',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='moderator',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='ndtDuration',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='paymentRecieved',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='resultReference',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='sponsorCompany',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='sponsorName',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='psl30initialform',
            name='sponsorTelephone',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]