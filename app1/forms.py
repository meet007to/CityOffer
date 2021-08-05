from django import forms
from .models import Customer, ShopKeeper


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class ShopKeeperForm(forms.ModelForm):
    class Meta:
        model = ShopKeeper
        fields = "__all__"
