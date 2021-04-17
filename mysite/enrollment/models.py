from django.db import models
from students.models import Student
from courses.models import Courses
# Create your models here.
class Enrollment(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    student = models.ForeignKey(Student,related_name="enrollment_student",null=True, blank=True , on_delete=models.CASCADE)
    course = models.ForeignKey(Courses,related_name="enrollment_course",null=True, blank=True , on_delete=models.CASCADE)
    exam_date = models.DateTimeField(auto_now_add=True)
    # student = models.ForeignKey(Teacher,related_name="teacher_cer",null=True, blank=True , on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'enrollment'
