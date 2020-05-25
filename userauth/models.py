from django.db import models
from django.contrib.auth.models import AbstractUser
                             
from authapp_api_and_backend import helper
# Create your models here.

                             
                             
class User(AbstractUser):
    """Extend functionality of user"""
                            
    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)
    full_name = models.CharField(max_length=50, default="full name") 
    isProvider = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    