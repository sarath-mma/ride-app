from django.contrib.gis.db import models
from driver.models import Base, Driver, Location
from django.utils.translation import gettext_lazy as _
import binascii
import os
from django.contrib.auth.hashers import make_password
# Create your models here.

STATUS = (
    ('0', 'pending'),
    ('1', 'started'),
    ('2', 'completed'),
    ('3', 'cancelled'),
)

DRV_STATUS =(
    ('0', 'REJECT'),
    ('1', 'ACCEPT'),
)

class CustomerManager(models.Manager):

    def create_customer(self, name, email, password):
        customer =  self.model(name=name, email=email, password=make_password(password))
        customer.save()
        return customer

class Customer(models.Model):

    name = models.CharField(_('Full name'), max_length = 255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length = 500)

    objects = models.Manager()
    customermanager = CustomerManager()

    def __str__(self):

        return self.name
    
    def is_authenticated(self):
        return False

class Ride(models.Model):

    customer = models.ForeignKey(Customer, related_name='customer_ride', on_delete=models.RESTRICT)
    driver = models.ForeignKey(Driver, related_name ='ride_driver', on_delete=models.RESTRICT)
    pickup_location = models.PointField()
    dropoff_location = models.PointField()
    status = models.CharField(max_length=255, choices=STATUS)
    accept = models.CharField(max_length=255, choices =DRV_STATUS, null=True, blank=True)

    def __str__(self):

        return self.customer.name
    

class TokenCustomer(models.Model):
    customer = models.OneToOneField(Customer, related_name='customertoken', on_delete=models.CASCADE)
    token =  models.CharField(_('key'), max_length=40, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.token)
    
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_key()
        return super().save(*args, **kwargs)
    
    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()


#using managed is False for creating searilizer fealds easy 
#not migrating this model 
    
class RideRequest(models.Model):
    customer = models.ForeignKey(Customer, related_name='cus_ridereq', on_delete =models.CASCADE)
    longitude = models.TextField()
    latitude = models.TextField()
    car_type = models.IntegerField(null = True, blank=True)
    seat_capacity = models.IntegerField(null = True, blank=True)
    boot_capacity = models.IntegerField(null = True, blank=True)

    class Meta:
        managed = False

