# Generated by Django 3.2.5 on 2021-10-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0041_auto_20211015_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='tescandidate',
            name='facebook',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='tescandidate',
            name='instagram',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='tescandidate',
            name='linkedin',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='tescandidate',
            name='skype',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='tescandidate',
            name='twitter',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]