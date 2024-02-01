from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from . models import Ride
from driver.models import Driver, Location, Vehicle
import random
class Ridematcher:

    def __init__(self, **kwargs):
        self.lon = kwargs['longitude']
        self.lat = kwargs['latitude']
        self.car_type = kwargs['car_type']
        self.seat_capacity = kwargs['seat_capacity']
        self.boot_capacity = kwargs['boot_capacity']

    
    @staticmethod
    def locatonCoder(lat, lon):
        return  Point(lon, lat, srid=4326)


    def get_vehicles(self):
        pickup_location = self.locatonCoder(float(self.lat[0]), float(self.lon[0]))
        #filtering distance radiours below 30KM
        queryset = Driver.objects.filter(
            pk__in = Vehicle.objects.all().values('driver'),
            id__in = Location.objects.all().values('driver')
        ).annotate(distance=Distance('driver_location__location', pickup_location)).filter(distance__lt=30000).order_by('distance')[0:6]

        return self.JsonConvert(queryset)
    

    def JsonConvert(self, data):
        myDict = []
        for item in data:
            distance = self.meterto_km(item.distance.m)
            dic = {
                'id':item.id,
                'distance': distance,
                'time_away_from_you': self.timeTake(distance, random.randint(1,3) ),
                'name':item.name,
                'brand': item.driver_vehicle.brand,
                'model': item.driver_vehicle.model,
                'reg_year': item.driver_vehicle.reg_year,
                'seat_capacity': item.driver_vehicle.seat_capacity,
                'boot': item.driver_vehicle.boot,
                'charge': item.driver_vehicle.charge
            }
            myDict.append(dic)

        return myDict
    
    @staticmethod
    def meterto_km(meter):
        return round(float(meter)/1000, 2)

    @staticmethod
    def timeTake(distance, trafic):
        time = ''
        #low trafic
        if trafic == 1:
            time= distance * 3
        #medium tramic
        elif trafic == 2:
            time = distance * 4
        #heigh trafic
        else:
            time = distance * 5

        if time > 60:
            return  int(time / 60) +''+ time % 60
        return str(round(time)) +' MIN'
        
        


        