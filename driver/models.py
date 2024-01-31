from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, FileExtensionValidator
import datetime
from django.contrib.auth.hashers import make_password
import binascii
import os
# Create your models here.

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '9999999999'. Up to 15 digits allowed.")

GENDERS = (
    ('0', 'male'),
    ('1', 'female'),
    ('2', 'others')
)

VEHICLE_TYPE = (
    ('0', 'sedan'),
    ('1', 'hatchback'),
    ('1', 'suv'),
)

SEATING_CAPACITY = (
    ('0', '4'),
    ('0', '7'),
)

BOOT_SPACE = (
    ('0', '330L'),
    ('1', '600L'),
    ('1', '1200L'),
)

class Base(models.Model):

    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True


class DriverManager(models.Manager):

    def create_driver(self, name, email, password):
        driver =  self.model(name=name, email=email, password=make_password(password))
        driver.save()
        return driver

class Driver(Base):

    name = models.CharField(_('Full name'), max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length = 500)

    objects = models.Manager()
    customermanager = DriverManager()

    def __str__(self):
        return self.name
    
    def is_authenticated(self):
        return False
    
class Vehicle(Base):

    driver = models.OneToOneField(Driver, related_name = 'driver_vehicle', on_delete = models.CASCADE)
    brand = models.CharField(_('Vehicle Brand'), max_length = 255)
    model = models.CharField(_('Vehicle Model'), max_length=255)
    reg_year = models.CharField(_('Vehicle Registerd Year'), max_length = 255, choices = [(f'{r}', r) for r in range(1990, int(datetime.date.today().year) + 1)])
    type = models.CharField(_('Vehicle Type'), max_length=255, choices = VEHICLE_TYPE)
    seat_capacity = models.CharField(_('Vehicle Seat Capacity'), max_length=255, choices=SEATING_CAPACITY)
    boot = models.CharField(_('Vehicle Boot Capacity'), max_length=255, choices=BOOT_SPACE)
    charge = models.IntegerField(_('Taxi charge/km'))

    def __str__(self):
        return self.driver.name
    
class Location(Base):

    driver = models.OneToOneField(Driver, related_name = 'driver_location', on_delete = models.CASCADE)
    location = models.PointField()

    def __str__(self):
        return self.driver.name


class TokenDriver(models.Model):
    driver = models.OneToOneField(Driver, related_name='drivertoken', on_delete=models.CASCADE)
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
    