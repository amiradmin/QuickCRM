# Generated by Django 3.2.5 on 2021-12-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0092_auto_20211201_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psl57a',
            name='dateOfCourse',
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
