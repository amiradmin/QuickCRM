# Generated by Django 4.0.4 on 2022-06-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0133_psl30initialform_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='ndtcovid19',
            name='candidate_confirmation',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
