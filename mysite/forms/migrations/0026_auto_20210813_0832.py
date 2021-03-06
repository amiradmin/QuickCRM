# Generated by Django 3.2.5 on 2021-08-13 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0037_candidateprofile_user'),
        ('forms', '0025_psl30logexp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='psl30logexp',
            old_name='fullname',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='psl30logexp',
            name='eventID',
        ),
        migrations.AddField(
            model_name='psl30logexp',
            name='event',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='osl_event', to='training.event'),
            preserve_default=False,
        ),
    ]
