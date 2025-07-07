from django.db import models
from users.models import User
from django.utils.crypto import get_random_string

# District Model
class District(models.Model):
    name = models.CharField(max_length=255, unique=True)
    district_code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.district_code}"

# Restaurant Model
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant')
    logo = models.ImageField(upload_to='restaurants/logos/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (owner - {self.owner.email})"

# RestaurantOutlet Model
class RestaurantOutlet(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='outlets')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='available_outlets')
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    outlet_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.outlet_code and self.restaurant and self.district:
            res_name = self.restaurant.name.upper().replace(" ","")
            dist_code = self.district.district_code.upper()
            random_code = get_random_string(length=4).upper()
            self.outlet_code = f"{res_name}-{dist_code}-{random_code}"
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f"Branch: {self.outlet_code}"

# OutletSchedule Model
class OutletSchedule(models.Model):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    DAYS_OF_WEEK = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]
    restaurant_outlet = models.ForeignKey(RestaurantOutlet, on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        unique_together = ('restaurant_outlet','day')
    
    def __str__(self):
        return f"{self.restaurant_outlet.outlet_code} - schedule"

# MoreInfo Model
class MoreInfo(models.Model):
    restaurant_outlet = models.OneToOneField(RestaurantOutlet, on_delete=models.CASCADE, related_name='info')
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    minimum_order = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    offer_text = models.CharField(max_length=50, null=True, blank=True)
    delivery_time = models.CharField(max_length=50, null=True, blank=True)
    is_featured = models.BooleanField(default=False) #Only admin can set
    is_active = models.BooleanField(default=True) #Only admin can change

    def __str__(self):
        return f"{self.restaurant_outlet.outlet_code} - more info"

# ContactInfo Model
class ContactInfo(models.Model):
    restaurant_outlet = models.OneToOneField(RestaurantOutlet, on_delete=models.CASCADE, related_name='contact_info')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    facebook_page = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    map_location_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Contact for {self.restaurant_outlet.outlet_code}"
