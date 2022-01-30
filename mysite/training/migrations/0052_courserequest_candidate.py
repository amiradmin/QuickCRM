# Generated by Django 3.2.5 on 2022-01-23 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training', '0051_courserequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserequest',
            name='candidate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candiate_request', to=settings.AUTH_USER_MODEL),
        ),
    ]
