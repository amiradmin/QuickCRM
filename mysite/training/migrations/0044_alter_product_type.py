# Generated by Django 3.2.5 on 2022-01-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0043_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
