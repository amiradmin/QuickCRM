# Generated by Django 3.2.5 on 2021-10-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_contact_formname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='formName',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
