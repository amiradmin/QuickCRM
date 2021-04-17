from django.db import models

# Create your models here.

class TeacherCertificate(models.Model):
    title = models.CharField(max_length=100)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'teacher_certificates'


class Teacher(models.Model):
    passport_id = models.CharField(max_length=100,blank=True, null=True)
    first_name = models.CharField(max_length=100,blank=True, null=True,)
    last_name = models.CharField(max_length=100,blank=True, null=True,)
    mobile = models.CharField(max_length=100,blank=True, null=True,)
    email = models.EmailField(max_length=100,blank=True, null=True,)
    address = models.CharField(max_length=100,blank=True, null=True,)
    certificates = models.ForeignKey(TeacherCertificate,related_name="teacher_cer",null=True, blank=True , on_delete=models.CASCADE)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    class Meta:
        db_table = 'teacher'
