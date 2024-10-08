from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views  import APIView
import datetime
from django.db import connection

# Create your views here.

class RateList(APIView):
    def get(self, request):
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')

        if not all([date_from, date_to, origin, destination]):
            return Response({'error': 'Missing required parameters'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            datetime.datetime.strptime(date_from, "%Y-%m-%d")
            datetime.datetime.strptime(date_to, "%Y-%m-%d")
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

        

        if(len(origin) == 5 and len(destination)==5):
            with connection.cursor() as cursor:
                cursor.callproc('public.get_average_prices_port_to_port', (origin, destination, date_from, date_to))
                results = cursor.fetchall()


        if(len(origin) == 5 and len(destination)> 5): #origin is port code, destination is region slug
            with connection.cursor() as cursor:
                cursor.callproc('public.get_average_prices_port_to_region', (origin, destination, date_from, date_to))
                results = cursor.fetchall()

        if(len(origin) > 5 and len(destination) == 5): #origin is region slug, destination is port code
            with connection.cursor() as cursor:
                cursor.callproc('public.get_average_prices_region_to_port', (origin, destination, date_from, date_to))
                results = cursor.fetchall()
        
        if(len(origin) > 5 and len(destination) > 5):
            with connection.cursor() as cursor:
                cursor.callproc('public.get_average_prices_region_to_region', (origin, destination, date_from, date_to))
                results = cursor.fetchall()
        

        average_prices = [{"day": row[1], "average_price": row[0]}  for row in results ]
        return Response (average_prices , status=status.HTTP_200_OK)