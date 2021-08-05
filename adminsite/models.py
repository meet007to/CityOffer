from django.db import models

# Create your models here


class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)


class Category(models.Model):
    catname = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.catname


class SubCategory(models.Model):
    catname = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    subname = models.CharField(max_length=50)

    def __str__(self):
        return self.subname
