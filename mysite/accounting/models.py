from django.db import models
from training .models import CandidateProfile
# Create your models here.
class Invoice(models.Model):
    STATUS_CHOICES = (('P', 'Partial Payment'), ('F', 'Fully Payment'))
    candidate = models.ForeignKey(CandidateProfile,related_name="can_invoice",  null=True, blank=True , on_delete=models.CASCADE)
    scanned_doc = models.FileField(upload_to='invoice_document',null=True,blank=True)
    receipt = models.FileField(upload_to='invoice_document',null=True,blank=True)
    balance = models.CharField(max_length=30, null=True, blank=True )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.user.first_name
