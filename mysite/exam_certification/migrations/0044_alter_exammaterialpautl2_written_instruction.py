# Generated by Django 4.0.1 on 2022-04-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_certification', '0043_alter_exammaterialpautl2_written_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammaterialpautl2',
            name='written_instruction',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
