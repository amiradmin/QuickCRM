# Generated by Django 3.2.5 on 2021-09-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0045_rename_debit_psl57b_debit'),
    ]

    operations = [
        migrations.CreateModel(
            name='emphistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(blank=True, max_length=512, null=True)),
                ('period', models.CharField(blank=True, max_length=512, null=True)),
                ('contactNamePhone', models.CharField(blank=True, max_length=512, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]