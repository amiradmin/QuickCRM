# Generated by Django 4.0.4 on 2022-09-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_submenulevelone_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenuleveltwo',
            name='href',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]