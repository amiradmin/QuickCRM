# Generated by Django 4.0.1 on 2022-03-12 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0127_candidateforms_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teslecfeedbackfrom',
            old_name='courseName',
            new_name='event',
        ),
    ]
