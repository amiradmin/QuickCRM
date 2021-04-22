from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=30, null=True, blank=True )
    passport_id = models.CharField(max_length=30, null=True, blank=True )
    twi_candidate_id = models.CharField(max_length=30, null=True, blank=True )
    sponsor_company = models.CharField(max_length=30, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    city = models.CharField(max_length=30,  null=True, blank=True  )
    country = models.CharField(max_length=30,  null=True, blank=True  )
    contact_number = models.CharField(max_length=30,  null=True, blank=True  )
    birth_date = models.DateField(null=True, blank=True)
    photo = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_1 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_2 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_3 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_4 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_5 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_6 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_7 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_8 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_9 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    avatar = models.FileField(upload_to='avatar',null=True,blank=True)
    note = models.TextField(max_length=2000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.first_name + ' ' + self.last_name
@receiver(post_save, sender=User)

def update_user_profile(sender, instance, created, **kwargs):
    if created:
        CandidateProfile.objects.create(user=instance)
    instance.candidateprofile.save()


class Product(models.Model):
    TYPE_CHOICES = (('V', 'Virtual Access'), ('C', 'Class Rooom Based'),('O', 'Online Zoom'))
    name = models.CharField(max_length=30, null=True, blank=True )
    code = models.CharField(max_length=30, null=True, blank=True )
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

class Location(models.Model):

    country = models.ForeignKey(Country,related_name="Country_location",  null=True, blank=True , on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    ANNOUNCMENT_CHOICES = (('S', 'SMS'), ('E', 'Email'))
    name = models.CharField(max_length=30, null=True, blank=True )
    product = models.ForeignKey(Product,related_name="product_event",  null=True, blank=True , on_delete=models.CASCADE)
    country = models.ForeignKey(Country,related_name="country_event",  null=True, blank=True , on_delete=models.CASCADE)
    location = models.ForeignKey(Location,related_name="location_event",  null=True, blank=True , on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)

    announcement_type =  models.CharField(max_length=1, choices=ANNOUNCMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
