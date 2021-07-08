from django.db import models

# Create your models here.


class Forms(models.Model):


    name = models.CharField(max_length=256, null=True, blank=True )
    dbName = models.CharField(max_length=256, null=True, blank=True )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name