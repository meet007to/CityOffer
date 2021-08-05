from django.urls import path
from .views import *

urlpatterns = [
    # ShopKeepers Urls
    path("", AdminLogin, name="adminlogin"),
    path("logout/", LogOut, name="logout"),
    path("shopkeeperlist/", ShopkeeperList, name="shopkeeperlist"),
    path("editshopkeeper/<str:email>/", EditShopkeeper, name="editshopkeeper"),
    path("updateshopkeeper/<str:email>/",
         UpdateShopKeeper, name="updateshopkeeper"),
    path("deleteshopkeeper/<str:email>/",
         DeleteShopKeeper, name="deleteshopkeeper"),

    # Customer Urls

    path("customerlist/", CustomerList, name="customerlist"),
    path("editcustomer/<str:email>/", EditCustomer, name="editcustomer"),
    path("updatecustomer/<str:email>/", UpdateCustomer, name="updatecustomer"),
    path("deletecustomer/<str:email>/",
         DeleteCustomer, name="deletecustomer"),

    # Catagory Urls
    path("categorylist/", CategoryList, name="catlist"),
    path("addcat/", AddCat, name="addcat"),
    path("editcat/<int:id>", EditCat, name="editcat"),
    path("deletecat/<int:id>", DeleteCat, name="deletecat"),

    # SubCategory URls
    path("subcategorylist/", SubCategoryList, name="sublist"),
    path("addsub/", AddSub, name="addsub"),
    path("editsub/<int:id>", EditSub, name="editsub"),
    path("deletesub/<int:id>", DeleteSub, name="deletesub"),

    # FeedBack Urls
    path("feedback/", FeedBack, name="feedback"),

    # Profile Url
    path("profile/", Profile, name="profile"),
    path("editprofile/<int:id>", EditProfile, name="editprofile"),


]
