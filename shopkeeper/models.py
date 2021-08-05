from django.db import models
from adminsite.models import Category, SubCategory
from app1.models import ShopKeeper
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    catname = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    subname = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        decimal_places=2, max_digits=20, default=100.00)
    chackedprise = models.DecimalField(
        decimal_places=2, max_digits=20, default=50.00)
    description = models.CharField(max_length=200, default="It for a ...")
    image = models.ImageField(upload_to="products", blank=True)
    status = models.CharField(max_length=10, default="A")
    email = models.ForeignKey(
        ShopKeeper, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __unicode__(self):
        return self.product
