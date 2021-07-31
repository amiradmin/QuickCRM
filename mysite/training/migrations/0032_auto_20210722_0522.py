# Generated by Django 3.2.4 on 2021-07-22 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0031_auto_20210721_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('colorCode', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MainForm',
        ),
        migrations.AddField(
            model_name='category',
            name='form',
            field=models.ManyToManyField(blank=True, null=True, to='training.FormsList'),
        ),
        migrations.AlterField(
            model_name='tescandidate',
            name='forms',
            field=models.ManyToManyField(blank=True, null=True, to='training.FormsList'),
        ),
    ]
