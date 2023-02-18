from django.forms import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "description": forms.TextInput(attrs={"class": "form-control"}),
        #     "date_create": forms.DateInput(attrs={"class": "form-control"}),
        # }