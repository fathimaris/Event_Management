from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_customer=models.BooleanField(default=False)



class Customer_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    email = models.EmailField()
    Full_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"



class Event_Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    District = models.CharField(max_length=255)
    Venue = models.CharField(max_length=255)
    Approval_Status = models.IntegerField(default=0)





# models.py

from django.db import models

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Completed', 'Completed'), ('Failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.user.email} - {self.transaction_id}"



from django.db import models

class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} on {self.date}"
