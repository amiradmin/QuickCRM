# Generated by Django 3.2.5 on 2022-01-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0104_auto_20211227_1359'),
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
