# Generated by Django 3.2.4 on 2021-07-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0030_auto_20210721_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('colorCode', models.CharField(blank=True, max_length=256, null=True)),
                ('temp', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.CharField(blank=True, choices=[('Standard', 'Standard'), ('TOFD', 'TOFD'), ('CSWIP', 'CSWIP'), ('LRUT', 'LRUT')], max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='tescandidate',
            name='forms',
            field=models.ManyToManyField(blank=True, null=True, to='training.MainForm'),
        ),
    ]
