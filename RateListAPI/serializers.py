from rest_framework import serializers
from .models import Regions

class RegionSerializer(serializers.ModelSerializer):
        class Meta:
            model: Regions
            fields: ['slug','name','parent_slug']
