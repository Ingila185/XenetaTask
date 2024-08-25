from django.db import models

# Create your models here.

class Regions(models.Model):
        slug = models.SlugField(max_length=50, primary_key=True)
        name = models.CharField(max_length = 100)
        parent_slug = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True) #if a region is deleted all ports within that region should also be deleted


class Ports(models.Model):
        code = models.CharField(max_length = 5)
        name = models.CharField(max_length = 100)
        parent_slug = models.ForeignKey(Regions, on_delete=models.PROTECT) 


class Prices(models.Model):
        orig_code = models.ForeignKey(Ports, on_delete=models.CASCADE, related_name='origin_prices')
        dest_code = models.ForeignKey(Ports , on_delete=models.CASCADE, related_name='destination_prices')
        day = models.DateField()
        price = models.IntegerField()

