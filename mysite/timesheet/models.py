from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Timesheet(models.Model):
    # STATUS_CHOICES = (('P', 'Partial Payment'), ('F', 'Fully Payment'))
    staff = models.ForeignKey(User,related_name="staff_timesheet",  null=True, blank=True , on_delete=models.CASCADE)
    from_date = models.DateTimeField(null=True,blank=True)
    to_date = models.DateTimeField(null=True,blank=True)
    duration = models.FloatField(null=True,blank=True)
    description = models.CharField(max_length=30, null=True, blank=True )
    approved = models.BooleanField(default=False, null=True, blank=True )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff.first_name