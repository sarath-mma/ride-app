from rest_framework import serializers
from . models import Driver, TokenDriver

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