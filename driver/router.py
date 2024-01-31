from rest_framework import routers
from . views import DriverView

router = routers.DefaultRouter()
router.register('sign-up', DriverView, 'customer')