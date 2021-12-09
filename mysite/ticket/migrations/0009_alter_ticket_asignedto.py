# Generated by Django 3.2.5 on 2021-11-01 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_auto_20210420_1201'),
        ('ticket', '0008_ticketanswer_asignedto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='asignedTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_asignedTO', to='staff.staff'),
        ),
    ]
