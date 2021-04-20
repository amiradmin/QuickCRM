from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=30, null=True, blank=True )
    passport_id = models.CharField(max_length=30, null=True, blank=True )
    sponsor_company = models.CharField(max_length=30, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    city = models.CharField(max_length=30,  null=True, blank=True  )
    country = models.CharField(max_length=30,  null=True, blank=True  )
    contact_number = models.CharField(max_length=30,  null=True, blank=True  )
    birth_date = models.DateField(null=True, blank=True)
    document_1 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_2 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_3 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_4 = models.FileField(upload_to='candidate_document',null=True,blank=True)
    document_5 = models.FileField(upload_to='candidate_document',null=True,blank=True)
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
