from django.test import TestCase
from .models import Driver, Location, Vehicle

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ride.ridematching import Ridematcher

# Create your tests here.
class TestDriver(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Driver = Driver.objects.create(name="anju", email='testpass@gmail.com', password='testpass')

    def test_has_name(self):
        self.assertEqual(self.Driver.name, "anju")

    def test_has_email(self):
        self.assertEqual(self.Driver.email, 'testpass@gmail.com')

    def test_str(self):
        expected = "anju"
        actual = str(self.Driver)

        self.assertEqual(expected, actual)


class DriverTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new driver object.
        """
        url = 'http://127.0.0.1:8000/driver/sign-up/'
        data = {'name': 'mathew','email':'mathew1@gmail.com', 'password':'12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Driver.objects.count(), 1)
        self.assertEqual(Driver.objects.get().name, 'mathew')


class RideMatcherTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.driver = Driver.objects.create(name="anju", email='testpass@gmail.com', password='testpass')
        cls.vehicle = Vehicle.objects.create(driver=cls.driver, brand='vw', model='ameo', reg_year='2022', type='0', seat_capacity='0', boot='0', charge= 100)
        cls.location = Location.objects.create(driver = cls.driver, location='SRID=4326;POINT (76.45923553339578 10.458692656383096)')
        cls.data =  {'longitude': [cls.location.location.coords[0]], 'latitude': [cls.location.location.coords[1]], 'car_type': '0', 'seat_capacity': '0', 'boot_capacity': '0'}

    def test_checkvalue(self):
        self.assertEqual(len(Ridematcher(**self.data).get_vehicles()), 1)
