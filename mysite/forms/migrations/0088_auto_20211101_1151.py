# Generated by Django 3.2.5 on 2021-11-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0087_auto_20211101_1148'),
    ]

    operations = [
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
