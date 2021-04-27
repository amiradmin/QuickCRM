from django.db import models
from django.contrib.auth.models import User
from training.models import Country,Location
# Create your models here.


class Invigilator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passport_id = models.CharField(max_length=30, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    city = models.CharField(max_length=30,  null=True, blank=True  )
    country = models.CharField(max_length=30,  null=True, blank=True  )
    contact_number = models.CharField(max_length=30,  null=True, blank=True  )
    photo = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_1 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_2 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_3 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_4 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_5 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_6 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_7 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_8 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_9 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    avatar = models.FileField(upload_to='avatar',null=True,blank=True)
    note = models.TextField(max_length=2000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' '+ self.user.last_name

class Exam(models.Model):
    # TYPE_CHOICES = (('V', 'Virtual Accademy'), ('C', 'Class Rooom Based'),('O', 'Online Zoom'))
    name = models.CharField(max_length=30, null=True, blank=True )
    code = models.CharField(max_length=30, null=True, blank=True )

    # /type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    ANNOUNCMENT_CHOICES = (('S', 'SMS'), ('E', 'Email'))
    name = models.CharField(max_length=30, null=True, blank=True )
    exam = models.ForeignKey(Exam,related_name="exam_event",  null=True, blank=True , on_delete=models.CASCADE)
    country = models.ForeignKey(Country,related_name="country_event_exam",  null=True, blank=True , on_delete=models.CASCADE)
    location = models.ForeignKey(Location,related_name="location_event_exam",  null=True, blank=True , on_delete=models.CASCADE)
    # lecturers = models.ForeignKey(Lecturer,related_name="lecturer_event",  null=True, blank=True , on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    film = models.FileField(upload_to='exam_film',null=True,blank=True)

    announcement_type =  models.CharField(max_length=1,null=True, blank=True, choices=ANNOUNCMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
