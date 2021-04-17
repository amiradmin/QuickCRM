from django.db import models
from Teachers.models import Teacher
from students.models import Student

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    duration = models.CharField(max_length=100,blank=True, null=True,)
    location = models.CharField(max_length=100,blank=True, null=True,)
    teacher = models.ForeignKey(Teacher,related_name="teacher_cer",null=True, blank=True , on_delete=models.CASCADE)
    # student = models.ForeignKey(Teacher,related_name="teacher_cer",null=True, blank=True , on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'course'
