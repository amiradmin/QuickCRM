# Generated by Django 3.2.5 on 2022-01-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0120_auto_20220123_1847'),
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
