# Generated by Django 4.0.4 on 2022-05-31 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0078_event_deliverymethod'),
        ('contacts', '0012_alter_contact_messagetype_alter_contact_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_contact', to='training.event'),
        ),
    ]
