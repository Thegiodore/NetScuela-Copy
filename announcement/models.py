from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Announcement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content