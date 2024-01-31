from django.urls import path, include
from . router import router
from .views import DriverLogin
urlpatterns = [
    path('login/', DriverLogin.as_view()),
    path('', include(router.urls))   
]