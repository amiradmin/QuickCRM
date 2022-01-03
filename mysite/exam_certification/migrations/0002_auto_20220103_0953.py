# Generated by Django 3.2.5 on 2022-01-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='name',
            new_name='invigilator',
        ),
        migrations.AddField(
            model_name='exam',
            name='sequence',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='venue',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
