# Generated by Django 3.2.5 on 2021-10-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0069_alter_psl57b_emphistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='psl30logexp',
            name='totalHours',
            field=models.IntegerField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
    ]