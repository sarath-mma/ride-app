from django.shortcuts import render
from rest_framework import viewsets, views, permissions, generics

from ride.models import Ride
from . drivertokenauth import driverTokenAuth, CustomPermission
from . models import Driver, Location, TokenDriver, Vehicle
from . serializer import DriverSerializer, RideSerializer, VehicleSerializer, LocationSerializer
from rest_framework.response import Response
from . driverauthtokenserializer import RiderAuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class DriverView(viewsets.ModelViewSet):

    authentication_classes = [driverTokenAuth]
    permission_classes = [CustomPermission]
    queryset = Driver.objects.all()
    serializer_class  = DriverSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.action == "create": 
            return [permissions.AllowAny()]
        return super().get_permissions()
    

    def list(self, request, *args, **kwargs):
        query = Driver.objects.all()
        serializer = DriverSerializer(query, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serilize = DriverSerializer(data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response({'data': serilize.data, 'success': True})
        return Response({'data': serilize.errors, 'success': False})
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serilize = DriverSerializer(instance=instance, data=request.data, partial=True)
        if serilize.is_valid():
            serilize.save()
            return Response({'data': serilize.data, 'success': True})
        return Response({'data': serilize.errors, 'success': False})
    

class DriverLogin(ObtainAuthToken):

    serializer_class = RiderAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if TokenDriver.objects.filter(driver=user).exists():
                token = TokenDriver.objects.get(driver=user)
            else:
                token = TokenDriver.objects.create(driver=user)
            return Response({
                'status': True,
                'token': token.token,
                'id': user.pk,
                'username': user.email
            })
        else:
            return Response({
                'status': False
            })
        

class DriverVehicleViewSet(viewsets.ModelViewSet):
    authentication_classes = [driverTokenAuth]
    permission_classes = [CustomPermission]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_field = 'driver'

    def create(self, request, *args, **kwargs):
        serilize = VehicleSerializer(data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response({'data': serilize.data, 'success': True})
        return Response({'data': serilize.errors, 'success': False})
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serilize = VehicleSerializer(instance=instance, data=request.data, partial=True)
        if serilize.is_valid():
            serilize.save()
            return Response({'data': serilize.data, 'success': True})
        return Response({'data': serilize.errors, 'success': False})
    


class DriverLocationViewSet(viewsets.ModelViewSet):
    authentication_classes = [driverTokenAuth]
    permission_classes = [CustomPermission]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    lookup_field = 'driver'

    def create(self, request, *args, **kwargs):
        serilize = LocationSerializer(data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response({'data': serilize.data, 'success': True})
        return Response({'data': serilize.errors, 'success': False})
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serilize = LocationSerializer(instance=instance, data=request.data, partial=True)
        if serilize.is_valid():
            serilize.save()
            return Response({'data': serilize.data, 'success': True})
        return Response({'data': serilize.errors, 'success': False})
    

class DriverReideViewSet(viewsets.ModelViewSet):
    authentication_classes = [driverTokenAuth]
    permission_classes = [CustomPermission]
    serializer_class = RideSerializer
    queryset = Ride.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        driver = self.request.query_params.get('driver')
        query = Ride.objects.filter(driver=driver, accept=None)
        serializer = RideSerializer(query, many=True)
        return Response(serializer.data)


    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serilize = RideSerializer(instance=instance, data=request.data, partial=True)
        if serilize.is_valid():
            driver = serilize.validated_data['driver']
            if instance.driver == driver:
                serilize.save()
                return Response({'data': serilize.data, 'success': True})
            else:
                return Response({'data': 'You don\'t have permission to update' , 'success': False})
        return Response({'data': serilize.errors, 'success': False})
        