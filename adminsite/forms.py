from django import forms
from .models import Category, SubCategory, Admin


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class SubForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = "__all__"


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
