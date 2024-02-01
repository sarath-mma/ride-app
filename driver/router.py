from rest_framework import routers
from . views import DriverLocationViewSet, DriverView, DriverVehicleViewSet, DriverReideViewSet

router = routers.DefaultRouter()
router.register('sign-up', DriverView, 'driver')
router.register('add-vehicle', DriverVehicleViewSet, 'drivervehicle')
router.register('add-current-location', DriverLocationViewSet, 'addcurrentlocation')
router.register('get-driver-ride-request', DriverReideViewSet, 'ride')