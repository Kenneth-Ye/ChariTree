from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.
class User_transaction(models.Model):
    create_date = models.DateField(default = date.today)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_transactions')
    charity = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_transactions') 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.id)

class Charity_transaction(models.Model):
    create_date = models.DateField(default = date.today)
    # username of account that donates
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='charity_sent_transactions')
    # wallet of cause or charity
    cause = models.ForeignKey('Cause', on_delete=models.CASCADE, related_name='received_transactions') 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.id)

class Cause(models.Model):
    is_approved = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    charity = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='causes')
    wallet_addr = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name



