from django.urls import path, include
from . router import router
from .views import CustomerLogin
urlpatterns = [
    path('login/', CustomerLogin.as_view()),
    path('', include(router.urls))   
]