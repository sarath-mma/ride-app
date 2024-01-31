from rest_framework import routers
from . views import CustomerView

router = routers.DefaultRouter()
router.register('sign-up', CustomerView, 'customer')