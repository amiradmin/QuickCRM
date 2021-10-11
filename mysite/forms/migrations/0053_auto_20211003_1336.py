# Generated by Django 3.2.5 on 2021-10-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0052_auto_20211003_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='ControllingTheClass',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='ControllingTheClassComment',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='anyComments',
            field=models.CharField(blank=True, max_length=4092, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='appropriateAids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='appropriateAidsComment',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='generalBehaviour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='generalBehaviourComment',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='industrialExperience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='industrialExperienceComment',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='participantsAttraction',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='participantsAttractionComment',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='punctuality',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='punctualityComment',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='transposition',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='transpositionComment',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='usefulExample',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teslecfeedbackfrom',
            name='usefulExampleComment',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
    ]