from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Section(models.Model):
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'section'


class Staff(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True, null=True,)
    last_name = models.CharField(max_length=100,blank=True, null=True,)
    temp = models.CharField(max_length=100,blank=True, null=True,)
    mobile = models.CharField(max_length=100,blank=True, null=True,)
    email = models.EmailField(max_length=100,blank=True, null=True,)
    address = models.CharField(max_length=100,blank=True, null=True,)
    section = models.ForeignKey(Section,related_name="csection_stu",null=True, blank=True , on_delete=models.CASCADE)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


# 
# @receiver(post_save, sender=User)
# def update_user_staff(sender, instance, created, **kwargs):
#     if created:
#         Staff.objects.create(user=instance)
#     instance.staff.save()
