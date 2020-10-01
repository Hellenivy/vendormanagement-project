
from django.contrib import admin
from .models import ShippingProvider,Delivery,DispenserCoolerBox
# Register your models here.
admin.site.register(ShippingProvider)
admin.site.register(Delivery)
admin.site.register(DispenserCoolerBox)
