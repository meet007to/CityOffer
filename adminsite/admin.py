from django.contrib import admin
from .models import Category, SubCategory, Admin

# Register your models here.


class AppAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "password"]


admin.site.register(Admin, AppAdmin)


class AppCategory(admin.ModelAdmin):
    list_display = ["catname"]


admin.site.register(Category, AppCategory)


class AppSubCategory(admin.ModelAdmin):
    list_display = ["catname", "subname"]


admin.site.register(SubCategory, AppSubCategory)
