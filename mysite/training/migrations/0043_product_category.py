# Generated by Django 3.2.5 on 2022-01-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0042_auto_20211015_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
