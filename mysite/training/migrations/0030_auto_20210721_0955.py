# Generated by Django 3.2.4 on 2021-07-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0029_event_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='candidates',
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='events',
            field=models.ManyToManyField(to='training.Event'),
        ),
        migrations.AddField(
            model_name='skill',
            name='aboutMe',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='address',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='certificates',
            field=models.ManyToManyField(blank=True, null=True, to='training.Certificate'),
        ),
        migrations.AddField(
            model_name='skill',
            name='contact_number',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='customer_id',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_1',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_10',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_2',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_3',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_4',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_5',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_6',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_7',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_8',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='document_9',
            field=models.FileField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='first_name',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='last_name',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='candidate_document'),
        ),
        migrations.AddField(
            model_name='skill',
            name='postal_code',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='project',
            field=models.ManyToManyField(blank=True, null=True, to='training.CandidateProject'),
        ),
        migrations.AddField(
            model_name='skill',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='training.Skill'),
        ),
        migrations.AddField(
            model_name='skill',
            name='sponsor_company',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='tes_candidate_id',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='workHistory',
            field=models.ManyToManyField(blank=True, null=True, to='training.WorkHistory'),
        ),
        migrations.CreateModel(
            name='TesCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('customer_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('first_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('last_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('middleName', models.CharField(blank=True, max_length=1024, null=True)),
                ('tes_candidate_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('sponsor_company', models.CharField(blank=True, max_length=1024, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=128, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=1024, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('aboutMe', models.CharField(blank=True, max_length=5000, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='candidate_document')),
                ('document_1', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_2', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_3', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_4', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_5', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_6', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_7', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_8', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_9', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('document_10', models.FileField(blank=True, null=True, upload_to='candidate_document')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('certificates', models.ManyToManyField(blank=True, null=True, to='training.Certificate')),
                ('project', models.ManyToManyField(blank=True, null=True, to='training.CandidateProject')),
                ('skills', models.ManyToManyField(blank=True, null=True, to='training.Skill')),
                ('workHistory', models.ManyToManyField(blank=True, null=True, to='training.WorkHistory')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='candidate',
            field=models.ManyToManyField(blank=True, null=True, to='training.TesCandidate'),
        ),
    ]
