# Generated by Django 3.2.5 on 2021-09-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0048_auto_20210923_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visiontest',
            old_name='cerAddress',
            new_name='address',
        ),
        migrations.AddField(
            model_name='visiontest',
            name='colourPerception',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='employer',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='nearVisionAcuity',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='phone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='pslCerAddress',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='recognisedDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='recognisedLicenceNumber',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='recognisedName',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='recognisedOrganisation',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='recognisedPhone',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='shadesOfGrey',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='visiontest',
            name='tumbling',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
    ]
