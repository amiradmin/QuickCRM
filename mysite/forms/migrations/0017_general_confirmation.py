# Generated by Django 3.2.4 on 2021-07-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0016_general_formcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='confirmation',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
