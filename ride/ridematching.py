from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from . models import Ride
from driver.models import Driver, Location, Vehicle

class Ridematcher:

    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat
        # self.car_type = car_type
        # self.seat_capacity = seat_capacity
        # self.boot_capacity = boot_capacity

    
    @staticmethod
    def locatonCoder(lat, lon):
        return  Point(lon, lat, srid=4326)


    def get_vehicles(self):
        
        pickup_location = self.locatonCoder(self.lat, self.lon)
        queryset = Location.objects.annotate(distance=Distance('location', pickup_location)).order_by('distance')[0:6]
        return queryset


        