from django.db import models
from training.models import TesCandidate
# Create your models here.
class Contact(models.Model):
    TYPE_CHOICES = (('Admin', 'Admin'), ('Candidate', 'Candidate'))
    MESSAGE_TYPE_CHOICES = (('Form', 'Form'), ('Message', 'Message'))
    candidate = models.ForeignKey(TesCandidate, on_delete=models.CASCADE, null=True, blank=True)
    department = models.CharField(max_length=256, null=True, blank=True)
    message = models.CharField(max_length=4092, null=True, blank=True)
    type = models.CharField(choices=TYPE_CHOICES,max_length=10, null=True, blank=True)
    messageType = models.CharField(choices=MESSAGE_TYPE_CHOICES,max_length=10, null=True, blank=True)
    readFlag = models.BooleanField(default=False,null=True, blank=True)
    archived = models.BooleanField(default=False,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.first_name
