# Generated by Django 3.2.5 on 2021-11-29 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0090_auto_20211112_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgasexperienceform',
            name='sponsorAddress',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='sponsorCcmpany',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='bgasexperienceform',
            name='sponsorName',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='ndtcovid19',
            name='employeer',
            field=models.CharField(blank=True, max_length=512, null=True),
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