from rest_framework import serializers
from . models import Driver, TokenDriver, Vehicle, Location
from ride.models import Ride

class DriverSerializer(serializers.ModelSerializer):
    token =  serializers.StringRelatedField(many=False, read_only=True, source = 'agenttoken.token')
    class Meta:
        model = Driver
        exclude = ['created_at', 'updated_at']
        extra_kwargs  = {'password': {'write_only': True}}

    def create(self, validated_data):
        driver = Driver.customermanager.create_driver(**validated_data)
        TokenDriver.objects.create(driver=driver)
        return driver
    

class VehicleSerializer(serializers.ModelSerializer):
    driver_name = serializers.StringRelatedField(many=False, read_only = True, source = 'driver')
    class Meta:
        model = Vehicle
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    driver_name = serializers.StringRelatedField(many=False, read_only = True, source = 'driver')
    driver_detaisl = DriverSerializer(many=False, read_only = True, source = 'driver')
    class Meta:
        model = Location
        fields = '__all__'


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'