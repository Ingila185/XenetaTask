from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views  import APIView

# Create your views here.

@api_view()
def rates(request):
    return Response('Average port rates from origin to destination', status=status.HTTP_200_OK)

class RateList(APIView):
    def get(self, request):
        return Response ({"message:": "Average port rates from origin to destination - Class"}, status=status.HTTP_200_OK)