# Generated by Django 3.2.5 on 2021-10-27 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0042_auto_20211015_0816'),
        ('forms', '0072_alter_psl57b_emphistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psl57b',
            name='emphistory',
            field=models.ManyToManyField(blank=True, null=True, to='forms.empHistory'),
        ),
        migrations.CreateModel(
            name='PSL57A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactMe', models.BooleanField(blank=True, null=True)),
                ('cerAddress', models.CharField(blank=True, max_length=2048, null=True)),
                ('pslCerAddress', models.CharField(blank=True, max_length=2048, null=True)),
                ('phone', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Femail')], max_length=1, null=True)),
                ('pclNumber', models.CharField(blank=True, max_length=1024, null=True)),
                ('birthDay', models.DateField(blank=True, null=True)),
                ('currentEmploymentDetails', models.CharField(blank=True, max_length=1024, null=True)),
                ('candidatePosition', models.CharField(blank=True, max_length=512, null=True)),
                ('employmentStatus', models.CharField(blank=True, max_length=512, null=True)),
                ('examinationType', models.CharField(blank=True, max_length=512, null=True)),
                ('trainingOrg', models.CharField(blank=True, max_length=512, null=True)),
                ('dateOfCourse', models.DateField(blank=True, null=True)),
                ('iroductsIndustrySector', models.CharField(blank=True, max_length=1024, null=True)),
                ('NDTMethod', models.CharField(blank=True, max_length=256, null=True)),
                ('NDTLevel', models.CharField(blank=True, max_length=256, null=True)),
                ('ifLevel3', models.CharField(blank=True, max_length=256, null=True)),
                ('radiationSafety', models.CharField(blank=True, max_length=256, null=True)),
                ('radiationProtectionSup', models.CharField(blank=True, max_length=256, null=True)),
                ('categoriesOfCertification', models.CharField(blank=True, max_length=256, null=True)),
                ('preferredExaminationDateVenu', models.CharField(blank=True, max_length=1024, null=True)),
                ('claimDuration', models.CharField(blank=True, max_length=256, null=True)),
                ('verClaimAddress', models.CharField(blank=True, max_length=1024, null=True)),
                ('dateOfSign', models.DateField(blank=True, null=True)),
                ('sponsorName', models.CharField(blank=True, max_length=256, null=True)),
                ('sponsorCompany', models.CharField(blank=True, max_length=256, null=True)),
                ('sponsorPhone', models.CharField(blank=True, max_length=256, null=True)),
                ('sponsorSign', models.CharField(blank=True, max_length=256, null=True)),
                ('testCenterExamDate', models.DateField(blank=True, null=True)),
                ('testCenterVenue', models.CharField(blank=True, max_length=256, null=True)),
                ('testCenterExaminer', models.CharField(blank=True, max_length=256, null=True)),
                ('testCenterModerator', models.CharField(blank=True, max_length=256, null=True)),
                ('testCenterPaymentReceived', models.CharField(blank=True, max_length=256, null=True)),
                ('testCenterResultRef', models.CharField(blank=True, max_length=256, null=True)),
                ('testCenterExamCompleteColsed', models.CharField(blank=True, max_length=256, null=True)),
                ('nameAddressInvoice', models.CharField(blank=True, max_length=1024, null=True)),
                ('accommodation', models.CharField(blank=True, max_length=1024, null=True)),
                ('paymentMethod', models.CharField(blank=True, max_length=1024, null=True)),
                ('cheque', models.BooleanField(blank=True, null=True)),
                ('nameResponsible', models.CharField(blank=True, max_length=256, null=True)),
                ('companyOrderReference', models.CharField(blank=True, max_length=1024, null=True)),
                ('creditCardPayment', models.CharField(blank=True, max_length=256, null=True)),
                ('issueExpiryDates', models.DateField(blank=True, null=True)),
                ('NameOnCard', models.CharField(blank=True, max_length=256, null=True)),
                ('cardNumber', models.CharField(blank=True, max_length=256, null=True)),
                ('securityCode', models.CharField(blank=True, max_length=256, null=True)),
                ('addressCreditCardHolder', models.CharField(blank=True, max_length=256, null=True)),
                ('debit', models.CharField(blank=True, max_length=256, null=True)),
                ('confirmation', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_psl_57a', to='training.tescandidate')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_psl_57a', to='training.category')),
                ('emphistory', models.ManyToManyField(blank=True, null=True, to='forms.empHistory')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_psl_57a', to='training.event')),
                ('guideline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guideline_psl_57a', to='training.formslist')),
            ],
        ),
    ]
