from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ShippingProvider(models.Model):
    name = models.CharField(max_length=6)
    date_joined = models.DateTimeField()
    email = models.EmailField()
    transport_mode = models.CharField(max_length=6)
   

    def _str_(self):
        return self.name

class DispenserCoolerBox(models.Model):
    location = models.CharField(max_length=10)
   
    


class Delivery(models.Model):
    order = models.ForeignKey("self",on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    ShippingProvider = models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.ShippingProvider
