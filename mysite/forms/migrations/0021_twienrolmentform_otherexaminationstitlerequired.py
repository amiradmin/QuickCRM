# Generated by Django 3.2.5 on 2021-08-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0020_auto_20210803_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='twienrolmentform',
            name='otherExaminationsTitleRequired',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]