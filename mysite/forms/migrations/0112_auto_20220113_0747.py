# Generated by Django 3.2.5 on 2022-01-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0111_auto_20220112_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='psl57a',
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
