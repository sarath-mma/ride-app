from django.test import TestCase
from .models import Driver

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = 'http://127.0.0.1:8000/driver/sign-up/'
        data = {'name': 'mathew','email':'mathew1@gmail.com', 'password':'12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Driver.objects.count(), 1)
        self.assertEqual(Driver.objects.get().name, 'mathew')