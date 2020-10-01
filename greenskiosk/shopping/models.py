from django.db import models
from django.contrib.auth.models import User
from catalogue.models import Product

# Create your models here.
class Cart(models.Model):
    product=models.ManyToManyField(Product)
    date_created=models.DateTimeField()
    total_price=models.DecimalField(max_digits=6,decimal_places=2)
    status=models.CharField(max_length=7)


class Payment(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=6)
    order = models.ForeignKey("self",on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    date_of_payment = models.DateTimeField()

    def _str_(self):
        return self.order()

class Order(models.Model):
    customer = models.ForeignKey("self",on_delete=models.CASCADE)
    date_placed = models.DateTimeField()
    basket = models.ForeignKey(User,on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=6,decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6,decimal_places=2)

    def _str_(self):
        return self.customer()
