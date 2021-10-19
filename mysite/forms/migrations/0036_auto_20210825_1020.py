# Generated by Django 3.2.5 on 2021-08-25 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0040_alter_event_formcategory'),
        ('forms', '0035_auto_20210822_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='formlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_form', to='training.category'),
        ),
        migrations.AddField(
            model_name='formlist',
            name='guideline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guideline_form', to='training.formslist'),
        ),
    ]
