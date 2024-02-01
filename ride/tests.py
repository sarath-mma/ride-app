from django.test import TestCase
from .models import Customer

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class TestCustomer(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.customer = Customer.objects.create(name="anju", email='testpass@gmail.com', password='testpass')

    def test_has_name(self):
        self.assertEqual(self.customer.name, "anju")

    def test_has_email(self):
        self.assertEqual(self.customer.email, 'testpass@gmail.com')

    def test_str(self):
        expected = "anju"
        actual = str(self.customer)

        self.assertEqual(expected, actual)


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = 'http://127.0.0.1:8000/ride/sign-up/'
        data = {'name': 'mathew','email':'mathew1@gmail.com', 'password':'12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'mathew')