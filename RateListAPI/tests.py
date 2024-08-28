from django.test import TestCase, Client
from django.db import connection
from django.urls import reverse

from rest_framework.test import APIClient

# Create your tests here.
class RateListTestCase(TestCase):

    client = APIClient()

    def test_database_connection(self):
        with connection.cursor() as cursor:
            try:
                cursor.callproc('public.get_average_prices', (origin, destination, date_from, date_to))
            except ProgrammingError:
                self.fail("Stored procedure not found in test database")


    def test_get_average_prices_success(self):
        url = reverse('rates/')
        params = {
            'date_from': '2016-01-01',
            'date_to': '2016-01-10',
            'origin': 'CNSGH',
            'destination': 'BEZEE'}

        response = client.get(url, params)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 0)  # Ensure at least one result


    def test_get_average_prices_missing_params(self):
        response = client.get("")
        self.assertEqual(response.status_code, 400) # Ensure bad request is thrown

   
    def test_get_average_prices_invalid_date_format(self):
        url = ''
        params = {
            'date_from': 'Invalid Date',
            'date_to':'2016-01-01',
            'origin': 'CNSGH',
            'destination': 'BEZEE'
        }

        response = client.get(url)
        self.assertEqual(response.status_code, 400)  # Ensure bad request is thrown
