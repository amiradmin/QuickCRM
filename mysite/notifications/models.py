from django.db import models
from students.models import Student
# Create your models here.
class Notification(models.Model):

    title = models.CharField(max_length=100,blank=True, null=True,)
    text = models.TextField(max_length=2048,blank=True, null=True,)

    student = models.ForeignKey(Student,related_name="stu_message",null=True, blank=True , on_delete=models.CASCADE)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    class Meta:
        db_table = 'notification'
