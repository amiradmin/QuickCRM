# Generated by Django 3.2.5 on 2021-10-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0062_alter_psl57b_emphistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
    ]
