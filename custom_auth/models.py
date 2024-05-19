from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_charity = models.BooleanField(default=False)
    wallet_addr = models.CharField(max_length=100, blank=True, null=True)

    #new params
    text_desc = models.TextField(max_length=500, blank=True, null=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.username

