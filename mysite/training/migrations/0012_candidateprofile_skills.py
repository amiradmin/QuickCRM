# Generated by Django 3.2.4 on 2021-06-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0011_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='training.Skill'),
        ),
    ]
