from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import check_password

class RiderAuthTokenSerializer(AuthTokenSerializer):

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        print(username)
        print(password)
        if username and password:
            try:
                org = Customer.objects.get(email=username)
                valid = check_password(password, org.password)
                if valid:
                    user = org
                else:
                    user = None
            except Customer.DoesNotExist:
                user = None
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        
        attrs['user'] = user
        return attrs