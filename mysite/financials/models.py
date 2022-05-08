from django.db import models
from django.contrib.auth.models import User
from training.models import Country,Location,TesCandidate,Product,Event





class EventCandidatePayment(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="event_payment", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="candidate_payment",  null=True, blank=True , on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=512, null=True, blank=True)
    company_address = models.CharField(max_length=1024, null=True, blank=True)
    post_code = models.CharField(max_length=512, null=True, blank=True)
    phone = models.CharField(max_length=512, null=True, blank=True)
    fax = models.CharField(max_length=512, null=True, blank=True)
    contact_name = models.CharField(max_length=512, null=True, blank=True)
    email = models.CharField(max_length=512, null=True, blank=True)
    sponsor_status = models.BooleanField(default=False, null=True, blank=True)
    payment_status =  models.CharField(max_length=512, null=True, blank=True)
    invoiced_file = models.FileField(upload_to='exam_file', null=True, blank=True)
    recipients_file = models.FileField(upload_to='exam_file', null=True, blank=True)

    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
