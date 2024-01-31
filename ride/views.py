from django.shortcuts import render
from rest_framework import viewsets, views, permissions, generics
from . ridertokenauth import riderTokenAuth, CustomPermission
from . models import Customer, TokenCustomer
from . serializer import CustomerSerializer
from rest_framework.response import Response
from . riderauthtokenserializer import RiderAuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class CustomerView(viewsets.ModelViewSet):

    authentication_classes = [riderTokenAuth]
    permission_classes = [CustomPermission]
    queryset = Customer.objects.all()
    serializer_class  = CustomerSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.action == "create": 
            return [permissions.AllowAny()]
        return super().get_permissions()
    

    def list(self, request, *args, **kwargs):
        query = Customer.objects.all()
        serializer = CustomerSerializer(query, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serilize = CustomerSerializer(data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response({'data': serilize.data, 'success': True})
        return Response({'data': serilize.errors, 'success': False})
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serilize = CustomerSerializer(instance=instance, data=request.data, partial=True)
        if serilize.is_valid():
            serilize.save()
            return Response({'data': serilize.data, 'success': True})
        return Response({'data': serilize.errors, 'success': False})
    

class CustomerLogin(ObtainAuthToken):

    serializer_class = RiderAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if TokenCustomer.objects.filter(customer=user).exists():
                token = TokenCustomer.objects.get(customer=user)
            else:
                token = TokenCustomer.objects.create(customer=user)
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
        