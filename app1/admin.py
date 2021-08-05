from django.contrib import admin
from .models import Customer, ShopKeeper, Order

# Register your models here.


class AppCustomer(admin.ModelAdmin):
    list_display = [
        "firstname", "cemail", "lastname", "dob", "gender", "address", "mobile", "pincode", "state", "city", "cimage", "status"
    ]


class AppShopKeeper(admin.ModelAdmin):
    list_display = [
        "semail", "shopname", "firstname", "lastname", "dob", "gender", "address", "mobile", "pincode", "state", "city", "simage", "status"
    ]


class AppOrder(admin.ModelAdmin):
    list_display = [
        "semail", "cemail", "name", "price", "quantity", "status"
    ]


admin.site.register(Order, AppOrder)
admin.site.register(Customer, AppCustomer)
admin.site.register(ShopKeeper, AppShopKeeper)
