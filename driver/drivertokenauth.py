from rest_framework.authentication import TokenAuthentication, get_authorization_header
from . models import TokenDriver
from rest_framework import  exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated

class driverTokenAuth(TokenAuthentication):

    def get_model(self):
        return TokenDriver
    
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('driver').get(token=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        # if not token.user.is_active:
        #     raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.driver, token)
    

class CustomPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)