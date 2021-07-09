# Generated by Django 3.2.4 on 2021-07-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_fields'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fields',
            new_name='Field',
        ),
        migrations.AddField(
            model_name='forms',
            name='fields',
            field=models.ManyToManyField(blank=True, null=True, to='forms.Field'),
        ),
    ]
