from stafftimesheet.models import Timesheet
from django.db import models
from datetime import datetime 

class TimesheetChecker(models.Model):
    date = models.DateTimeField()
    trigger = models.BooleanField(default=False,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.date)
