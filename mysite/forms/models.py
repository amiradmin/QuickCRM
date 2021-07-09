from django.db import models

# Create your models here.

class Field(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    type = models.CharField(max_length=256, null=True, blank=True )
    label = models.CharField(max_length=256, null=True, blank=True )
    require = models.BooleanField(null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Forms(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    dbName = models.CharField(max_length=256, null=True, blank=True )
    fields = models.ManyToManyField( 'Field',null=True, blank=True )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
