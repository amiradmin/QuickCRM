# Generated by Django 4.0.1 on 2022-02-04 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0057_remove_staffprofile_currentcompany_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserequest',
            name='candidate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candiate_request', to='training.tescandidate'),
        ),
    ]