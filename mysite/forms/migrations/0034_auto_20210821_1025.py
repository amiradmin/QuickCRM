# Generated by Django 3.2.5 on 2021-08-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0033_auto_20210821_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psl30initialform',
            name='basicRadiationSafty',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='psl30initialform',
            name='radiationProtectionSupervisor',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
