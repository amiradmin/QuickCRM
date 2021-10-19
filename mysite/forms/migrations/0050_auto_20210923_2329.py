# Generated by Django 3.2.5 on 2021-09-23 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0049_auto_20210923_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visiontest',
            name='pslCerAddress',
        ),
        migrations.AddField(
            model_name='visiontest',
            name='birthDay',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
    ]
