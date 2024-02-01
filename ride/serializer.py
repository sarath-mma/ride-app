from rest_framework import serializers
from . models import Customer, Ride, RideRequest, TokenCustomer
from driver.serializer import LocationSerializer

class CustomerSerializer(serializers.ModelSerializer):
    token =  serializers.StringRelatedField(many=False, read_only=True, source = 'agenttoken.token')
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs  = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = Customer.customermanager.create_customer(**validated_data)
        TokenCustomer.objects.create(customer=customer)
        return customer
    

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'