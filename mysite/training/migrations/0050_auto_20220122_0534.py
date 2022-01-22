# Generated by Django 3.2.5 on 2022-01-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0049_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]