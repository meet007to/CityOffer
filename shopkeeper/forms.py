from django import forms
from .models import Product
from adminsite.models import SubCategory, Category


class ProductForm(forms.ModelForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #         'id': 'email', 'placeholder': 'Email', 'value': '{{ request.session.email }}', 'required': True}))
    class Meta:
        model = Product
        fields = ('name', 'catname', 'subname', 'quantity',
                  'price', 'chackedprise', 'description', 'image', 'email')

        widgets = {
            'email': forms.TextInput(attrs={'type': 'hidden'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subname'].queryset = SubCategory.objects.none()

        if 'catname' in self.data:
            try:
                catname_id = int(self.data.get('catname'))
                self.fields['subname'].queryset = SubCategory.objects.filter(
                    catname_id=catname_id).order_by('subname')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['subname'].queryset = self.instance.catname.subname_set.order_by(
        #         'subname')


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
