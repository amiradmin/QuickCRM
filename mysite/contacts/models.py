from django.db import models
from training.models import TesCandidate,Event
# Create your models here.
class Contact(models.Model):
    TYPE_CHOICES = (('Admin', 'Admin'), ('Candidate', 'Candidate'), ('Site', 'Site'))
    MESSAGE_TYPE_CHOICES = (('Form', 'Form'), ('Message', 'Message'), ('Site', 'Site'))
    candidate = models.ForeignKey(TesCandidate, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event,related_name="event_contact",  null=True, blank=True , on_delete=models.CASCADE)
    department = models.CharField(max_length=256, null=True, blank=True)
    formName = models.CharField(default=None,max_length=256, null=True, blank=True)
    message = models.CharField(max_length=4092, null=True, blank=True)
    url = models.CharField(max_length=1024, null=True, blank=True)
    type = models.CharField(choices=TYPE_CHOICES,max_length=10, null=True, blank=True)
    objID = models.IntegerField( null=True, blank=True)
    messageType = models.CharField(choices=MESSAGE_TYPE_CHOICES,max_length=10, null=True, blank=True)
    readFlag = models.BooleanField(default=False,null=True, blank=True)
    archived = models.BooleanField(default=False,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.candidate.first_name
