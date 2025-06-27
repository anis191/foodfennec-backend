from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    RESTAURANT_OWNER = 'Restaurant_Owner'
    CUSTOMER = 'Customer'
    DELIVERY_MAN = 'Delivery_Man'
    ROLE_CHOICES = [
        (RESTAURANT_OWNER, 'Restaurant_Owner'),
        (CUSTOMER, 'Customer'),
        (DELIVERY_MAN, 'Delivery_Man'),
    ]
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,null=True,blank=True,default=None)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
