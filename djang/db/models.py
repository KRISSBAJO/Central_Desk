from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # Assumes you have Pillow installed.
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)



