# Generated by Django 3.2.5 on 2022-01-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0114_auto_20220113_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='psl57b',
            name='dateOfSign',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='sponsorCompany',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='sponsorName',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='sponsorPhone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='sponsorSign',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='testCenterExamCompleteColsed',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='testCenterExamDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='testCenterExaminer',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='testCenterModerator',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='testCenterPaymentReceived',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='testCenterResultRef',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='psl57b',
            name='testCenterVenue',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='psl57a',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
    ]