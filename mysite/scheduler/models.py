from stafftimesheet.models import Timesheet
from django.db import models
from datetime import datetime 

class TimesheetChecker(models.Model):
    timesheet = models.ForeignKey(Timesheet, related_name="timesheet_scheduler", on_delete=models.CASCADE)
    trigger = models.BooleanField(default=False,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.timesheet.staff.first_name
