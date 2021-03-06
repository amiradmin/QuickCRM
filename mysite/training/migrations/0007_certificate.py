# Generated by Django 3.2.4 on 2021-06-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_auto_20210611_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('institute', models.CharField(blank=True, max_length=30, null=True)),
                ('expiryDate', models.DateTimeField(blank=True, null=True)),
                ('issueDate', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
