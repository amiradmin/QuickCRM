# Generated by Django 3.2.5 on 2021-10-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0056_auto_20211011_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
    ]
