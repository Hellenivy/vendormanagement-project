from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProductSupplier(models.Model):
    
    email = models.EmailField()

class Product (models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
    kiosk = models.CharField(max_length=6)
    supplier_price = models.DecimalField(max_digits=6,decimal_places=2)
    selling_price = models.DecimalField(max_digits=6,decimal_places=2)
    product_image = models.ImageField(upload_to = "images")

class ProductCategory(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    icon = models.ImageField()

class ProductReview(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    review = models.TextField()

    def _str_(self):
        return self.review