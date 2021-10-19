# Generated by Django 3.2.5 on 2021-09-17 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0040_alter_event_formcategory'),
        ('forms', '0040_ndtcovid19'),
    ]

    operations = [
        migrations.CreateModel(
            name='PSL57B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cerAddres', models.CharField(blank=True, max_length=2048, null=True)),
                ('pslCerAddres', models.CharField(blank=True, max_length=2048, null=True)),
                ('phone', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Femail')], max_length=1, null=True)),
                ('pslNumber', models.CharField(blank=True, max_length=1024, null=True)),
                ('birthDay', models.DateField(blank=True, null=True)),
                ('confirmation', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_psl_57b', to='training.tescandidate')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_psl_57b', to='training.category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_psl_57b', to='training.event')),
                ('guideline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guideline_psl_57b', to='training.formslist')),
            ],
        ),
    ]
