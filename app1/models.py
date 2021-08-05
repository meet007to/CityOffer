from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField(blank=True, default="2020-04-30")
    address = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    mobile = models.IntegerField()
    cemail = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    cimage = models.ImageField(upload_to="CustomerImage", blank=True)
    status = models.CharField(max_length=10, default="A", blank=True)

    def __str__(self):
        return self.cemail


class ShopKeeper(models.Model):
    shopname = models.CharField(unique=True, max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField(blank=True, default="2020-04-30")
    address = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    mobile = models.IntegerField()
    semail = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    simage = models.ImageField(upload_to="ShopKeeperImage/", blank=True)
    status = models.CharField(max_length=10, default="A", blank=True)

    def __str__(self):
        return self.semail


class Order(models.Model):
    semail = models.ForeignKey(
        ShopKeeper, on_delete=models.CASCADE, blank=True)
    cemail = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default="pending")
