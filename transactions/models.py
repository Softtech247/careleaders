from django.db import models
from django.utils import timezone
from adminapp.models import  User
from django.utils.crypto import get_random_string
import time

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, unique=True, default="Please leave blank, System autogenerate")
    transaction_date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField()
    description = models.CharField(max_length=50, blank=True)
 
    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, User: {self.user}, Amount: {self.amount}"
    
    def save(self, *args, **kwargs):
        year = str(time.localtime().tm_year)[-2:]
        month = str(time.localtime().tm_mon).zfill(2)
        current_time = str(int(time.time()))
        random_chars = get_random_string(length=3, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        transaction_id = year + month + current_time[-4:] + random_chars
            # Assign the transaction ID to the field
        self.transaction_id = transaction_id
        super().save(*args, **kwargs)

