# Generated by Django 4.0.4 on 2022-06-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0079_certificate_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
