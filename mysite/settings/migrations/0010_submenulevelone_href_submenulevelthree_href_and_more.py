# Generated by Django 4.0.4 on 2022-09-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_sidebar_href_alter_submenulevelone_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenulevelone',
            name='href',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='submenulevelthree',
            name='href',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='submenuleveltwo',
            name='href',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
