from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
     GENDERS=(
         ("m","male"),
         ("f","female")
     )
     gender = models.CharField(max_length=6, choices=GENDERS)
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     phone_number = models.IntegerField()
     date_of_birth = models.DateField()
     id_number = models.IntegerField()
     email = models.EmailField()

     def __str__(self):
         return self.name

class ShippingAddress(models.Model):
    Customer = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=6)
    notes = models.TextField()


