# Generated by Django 4.0.1 on 2022-03-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0004_certificatetype_rename_film_certificate_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='certificatetype',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]