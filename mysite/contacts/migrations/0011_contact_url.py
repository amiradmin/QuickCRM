# Generated by Django 4.0.1 on 2022-02-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_alter_contact_formname'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='url',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
