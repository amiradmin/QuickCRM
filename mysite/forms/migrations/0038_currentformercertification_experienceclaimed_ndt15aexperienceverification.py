# Generated by Django 3.2.5 on 2021-09-07 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0040_alter_event_formcategory'),
        ('forms', '0037_formlist_formid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentFormerCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methodLevel', models.CharField(blank=True, max_length=512, null=True)),
                ('SchemeCertifyingAuthority', models.CharField(blank=True, max_length=512, null=True)),
                ('ExpiryDate', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceClaimed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methodLevel', models.CharField(blank=True, max_length=512, null=True)),
                ('ExperienceClaimedSince', models.CharField(blank=True, max_length=512, null=True)),
                ('NumberOfNonths', models.IntegerField(blank=True, null=True)),
                ('DateOfExamination', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NDT15AExperienceVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidateID', models.CharField(blank=True, max_length=512, null=True)),
                ('descriptionOfExperience', models.CharField(blank=True, max_length=512, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('nameJobTitle', models.CharField(blank=True, max_length=512, null=True)),
                ('companyName', models.CharField(blank=True, max_length=512, null=True)),
                ('supervisionActivity', models.CharField(blank=True, max_length=512, null=True)),
                ('verEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('verDate', models.DateField(blank=True, null=True)),
                ('confirmation', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_ndt', to='training.tescandidate')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_ndt', to='training.category')),
                ('currentFormerCertification', models.ManyToManyField(blank=True, null=True, to='forms.CurrentFormerCertification')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_ndt', to='training.tescandidate')),
                ('experienceClaimed', models.ManyToManyField(blank=True, null=True, to='forms.ExperienceClaimed')),
                ('guideline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guideline_ndt', to='training.formslist')),
            ],
        ),
    ]
