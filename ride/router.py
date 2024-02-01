from rest_framework import routers
from . views import CustomerView, ReideRequestViewSet, ReideViewSet

router = routers.DefaultRouter()
router.register('sign-up', CustomerView, 'customer')
router.register('ride-request', ReideRequestViewSet, 'riderequest')
router.register('ride-creation', ReideViewSet, 'ride')