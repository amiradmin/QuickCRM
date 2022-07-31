from django.db import models
from django.contrib.auth.models import User,Group
from training.models import TesCandidate
# Create your models here.



class UserMonitor(models.Model):
    user = models.ForeignKey(User, related_name="statictics_user", null=True, blank=True, on_delete=models.DO_NOTHING)
    login_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class LastLogin(models.Model):
    user = models.ForeignKey(User, related_name="last_login_user", null=True, blank=True, on_delete=models.DO_NOTHING)
    login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
