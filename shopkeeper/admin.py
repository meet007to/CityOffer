from django.contrib import admin
from .models import Product, Cart
# Register your models here.


class AppProduct(admin.ModelAdmin):
    list_display = ["name", "catname", "subname"]


class AppCart(admin.ModelAdmin):
    list_display = ["name", "quantity", "price"]


admin.site.register(Cart, AppCart)
admin.site.register(Product, AppProduct)
