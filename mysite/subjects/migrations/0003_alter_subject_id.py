# Generated by Django 3.2 on 2021-04-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20210420_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
