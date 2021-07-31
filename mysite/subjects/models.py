from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'subject'
