from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class SubMenuLevelTwo(models.Model):
    group = models.ManyToManyField(Group,  null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True )
    code = models.CharField(max_length=512, null=True, blank=True )
    url = models.CharField(max_length=512, null=True, blank=True )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SubMenuLevelOne(models.Model):
    group = models.ManyToManyField(SubMenuLevelTwo,  null=True, blank=True)
    submenu = models.ManyToManyField(Group,  null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True )
    code = models.CharField(max_length=512, null=True, blank=True )
    url = models.CharField(max_length=512, null=True, blank=True )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Sidebar(models.Model):
    group = models.ManyToManyField(Group,  null=True, blank=True)
    submenu = models.ManyToManyField(SubMenuLevelOne,  null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
