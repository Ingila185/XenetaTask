from rest_framework import serializers
from .models import AveragePrice


class AveragePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AveragePrice
        price = serializers.IntegerField()
        day = serializers.DateField()
