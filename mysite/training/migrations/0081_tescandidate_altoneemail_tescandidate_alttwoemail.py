# Generated by Django 4.0.6 on 2022-08-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0080_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tescandidate',
            name='altOneEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tescandidate',
            name='altTwoEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
