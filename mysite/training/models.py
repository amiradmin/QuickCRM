from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Product(models.Model):
    TYPE_CHOICES = (('V', 'Virtual Accademy'), ('C', 'Class Rooom Based'),('O', 'Online Zoom'))
    name = models.CharField(max_length=30, null=True, blank=True )
    code = models.CharField(max_length=30, null=True, blank=True )
    price = models.CharField(max_length=30, null=True, blank=True )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):

    name = models.CharField(max_length=30, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Skill(models.Model):

    name = models.CharField(max_length=64, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WorkHistory(models.Model):

    name = models.CharField(max_length=64, null=True, blank=True )
    position = models.CharField(max_length=64, null=True, blank=True )
    webSite = models.CharField(max_length=64, null=True, blank=True )
    date = models.DateField(null=True, blank=True )
    discription = models.CharField(max_length=2024, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CandidateProject(models.Model):

    name = models.CharField(max_length=64, null=True, blank=True )
    client = models.CharField(max_length=64, null=True, blank=True )
    startDate = models.DateField(null=True, blank=True )
    dueDate = models.DateField(null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Location(models.Model):

    country = models.ForeignKey(Country,related_name="Country_location",  null=True, blank=True , on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True )
    address = models.CharField(max_length=1024, null=True, blank=True )
    postalCode = models.CharField(max_length=512, null=True, blank=True )
    log = models.CharField(max_length=30, null=True, blank=True )
    lat = models.CharField(max_length=30, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Lecturer(models.Model):
  
    first_name = models.CharField(max_length=30, null=True, blank=True )
    last_name = models.CharField(max_length=30, null=True, blank=True )
    passport_id = models.CharField(max_length=30, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    city = models.CharField(max_length=30,  null=True, blank=True  )
    country = models.CharField(max_length=30,  null=True, blank=True  )
    mobile = models.CharField(max_length=30,  null=True, blank=True  )
    contact_number = models.CharField(max_length=30,  null=True, blank=True  )
    address = models.CharField(max_length=1024,  null=True, blank=True  )
    birth_date = models.DateField(null=True, blank=True)
    events = models.ManyToManyField('Event')
    certificates = models.ManyToManyField('Certificate')
    aboutMe = models.CharField(max_length=5000, null=True, blank=True )
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
    document_10 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    note = models.TextField(max_length=2000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' '+ self.last_name



class Event(models.Model):
    ANNOUNCMENT_CHOICES = (('S', 'SMS'), ('E', 'Email'))
    name = models.CharField(max_length=30, null=True, blank=True )
    product = models.ForeignKey(Product,related_name="product_event",  null=True, blank=True , on_delete=models.CASCADE)
    country = models.ForeignKey(Country,related_name="country_event",  null=True, blank=True , on_delete=models.CASCADE)
    location = models.ForeignKey(Location,related_name="location_event",  null=True, blank=True , on_delete=models.CASCADE)
    lecturers = models.ForeignKey(Lecturer,related_name="lecturer_event",  null=True, blank=True , on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    # start_date = models.DateField(null=True, blank=True)

    announcement_type =  models.CharField(max_length=1,null=True, blank=True, choices=ANNOUNCMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CandidateProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=1024, null=True, blank=True )
    first_name = models.CharField(max_length=1024, null=True, blank=True )
    last_name = models.CharField(max_length=1024, null=True, blank=True )
    tes_candidate_id = models.CharField(max_length=1024, null=True, blank=True )
    sponsor_company = models.CharField(max_length=1024, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    city = models.CharField(max_length=1024,  null=True, blank=True  )
    country = models.CharField(max_length=1024,  null=True, blank=True  )
    address = models.CharField(max_length=1024,  null=True, blank=True  )
    postal_code = models.CharField(max_length=128,  null=True, blank=True  )
    contact_number = models.CharField(max_length=1024,  null=True, blank=True  )
    birth_date = models.DateField(null=True, blank=True)
    aboutMe = models.CharField(max_length=5000, null=True, blank=True )
    events = models.ManyToManyField('Event')
    skills = models.ManyToManyField('Skill',  null=True, blank=True)
    workHistory = models.ManyToManyField('WorkHistory',  null=True, blank=True)
    project = models.ManyToManyField('CandidateProject',  null=True, blank=True)
    certificates = models.ManyToManyField('Certificate',  null=True, blank=True )
    photo = models.ImageField(upload_to='candidate_document',null=True,blank=True)
    document_1 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_2 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_3 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_4 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_5 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_6 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_7 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_8 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_9 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_10 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.user.first_name + ' '+ self.user.last_name

# @receiver(post_save, sender=User)

# def update_user_candidateprofile(sender, instance, created, **kwargs):
#     if created:
#         CandidateProfile.objects.create(user=instance)
#     instance.candidateprofile.save()


class Certificate(models.Model):
    
    name = models.CharField(max_length=64, null=True, blank=True )
    institute = models.CharField(max_length=30, null=True, blank=True )
    expiryDate = models.DateTimeField(null=True, blank=True)
    issueDate = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name