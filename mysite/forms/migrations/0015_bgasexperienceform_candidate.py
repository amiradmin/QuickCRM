# Generated by Django 3.2.4 on 2021-07-27 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0034_rename_formtype_event_formcategory'),
        ('forms', '0014_general'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgasexperienceform',
            name='candidate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bgas_candidate', to='training.tescandidate'),
            preserve_default=False,
        ),
    ]
