from django.db import models
from training.models import TesCandidate
from staff.models import Staff
# Create your models here.


class TicketAnswer(models.Model):
    TYPE_STATUS = (('Done', 'Done'), ('OnProcess', 'OnProcess'), ('new', 'new'))

    title = models.CharField(max_length=256, null=True, blank=True)
    department = models.CharField(max_length=256, null=True, blank=True)
    message = models.CharField(max_length=4092, null=True, blank=True)
    status = models.CharField(choices=TYPE_STATUS,max_length=10, null=True, blank=True)
    readFlag = models.BooleanField(default=False,null=True, blank=True)
    archived = models.BooleanField(default=False,null=True, blank=True)
    fileOne = models.FileField(upload_to='tickets',null=True, blank=True)
    fileTwo = models.FileField(upload_to='tickets',null=True, blank=True)
    closeDate = models.DateField(auto_now_add=True)
    asignedTo = models.CharField(max_length=256, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title


class Ticket(models.Model):
    TYPE_STATUS = (('Done', 'Done'), ('OnProcess', 'OnProcess'), ('new', 'new'))

    TicketNumber = models.CharField(default='TESTIK-0',max_length=256, null=True, blank=True)
    candidate = models.ForeignKey(TesCandidate, related_name="ticke_can", on_delete=models.CASCADE)
    asignedTo = models.ForeignKey(Staff, related_name="ticket_asignedTO", on_delete=models.CASCADE, null=True, blank=True)
    # asignedTo = models.CharField(max_length=256, null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    department = models.CharField(max_length=256, null=True, blank=True)
    message = models.CharField(max_length=4092, null=True, blank=True)
    status = models.CharField(choices=TYPE_STATUS,max_length=10, null=True, blank=True)
    readFlag = models.BooleanField(default=False,null=True, blank=True)
    archived = models.BooleanField(default=False,null=True, blank=True)
    fileOne = models.FileField(default=False,null=True, blank=True)
    fileTwo = models.FileField(default=False,null=True, blank=True)
    closeDate = models.DateTimeField(auto_now_add=True)
    answer = models.ManyToManyField(TicketAnswer,  null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


