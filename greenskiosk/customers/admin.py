
# Register your models here.
from django.contrib import admin
from .models import Customer,ShippingAddress

admin.site.register(Customer)
admin.site.register(ShippingAddress)
