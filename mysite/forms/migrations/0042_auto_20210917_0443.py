# Generated by Django 3.2.5 on 2021-09-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0041_psl57b'),
    ]

    operations = [
        migrations.RenameField(
            model_name='psl57b',
            old_name='cerAddres',
            new_name='cerAddress',
        ),
        migrations.RenameField(
            model_name='psl57b',
            old_name='pslCerAddres',
            new_name='pslCerAddress',
        ),
        migrations.AddField(
            model_name='psl57b',
            name='contactMe',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
