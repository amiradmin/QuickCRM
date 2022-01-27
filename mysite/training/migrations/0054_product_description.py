# Generated by Django 4.0.1 on 2022-01-27 08:21

from django.db import migrations
import tinymce_4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0053_remove_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=tinymce_4.fields.TinyMCEModelField(default='test'),
            preserve_default=False,
        ),
    ]