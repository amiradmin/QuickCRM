from django.db import models
from django.contrib.auth.models import User
from training.models import Country,Location,TesCandidate,Product,Event





class EventCandidatePayment(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="event_payment", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="candidate_payment",  null=True, blank=True , on_delete=models.DO_NOTHING)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name
