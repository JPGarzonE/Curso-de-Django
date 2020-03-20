"""Users models."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """Profile model.
    
    Proxy model that extends the base data with other information.
    """

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    biography = models.TextField(blank = True)
    phone_number = models.CharField(max_length=20)

    picture = models.ImageField(upload_to='users/pictures',blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username

