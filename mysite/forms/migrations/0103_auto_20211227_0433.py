# Generated by Django 3.2.5 on 2021-12-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0102_auto_20211226_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgasexperienceform',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
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
