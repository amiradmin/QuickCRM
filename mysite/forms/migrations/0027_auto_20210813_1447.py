# Generated by Django 3.2.5 on 2021-08-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0026_auto_20210813_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psl30logexp',
            name='dateCandidateDeclaration',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psl30logexp',
            name='reviewerDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]