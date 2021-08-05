from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    path("", Index, name="index"),
    path("login.html/", LoginCustomer, name="login"),
    path("shopkeeperlogin.html/", LoginShopkeeper),
    path("cregistration.html/", CustomerRegistration, name="cregistration"),
    path("sregistration.html/", ShopkeeperRegistration),
    path("clogout/", Clogout, name="clogout"),
    path("productview/<int:id>", ProductView, name="productview"),
    path("cart/<int:id>", Cart, name="cart"),
    path('orders/', orders, name='corders'),
    path("cart_remove<int:id>", cart_remove, name="cart_remove"),
    path("filterproduct/<int:id>/<str:str>/",
         filterproduct, name="filterproduct"),
    path("chackout/", chackout, name="chackout"),
    path("cprofile/", Cprofile, name="cprofile")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
