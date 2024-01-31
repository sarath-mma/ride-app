from rest_framework.authentication import TokenAuthentication, get_authorization_header
from . models import TokenCustomer
from rest_framework import  exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated

class riderTokenAuth(TokenAuthentication):

    def get_model(self):
        return TokenCustomer
    
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('customer').get(token=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        # if not token.user.is_active:
        #     raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.customer, token)
    

class CustomPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)