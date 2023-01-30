from django import forms
from .models import Client

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "contact_person": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        attrs = {"class": "form-control"}
        widgets = {}
        for field in ['name', "address", "contact_person", "phone", "email"]:
            if field == "email":
                widgets[field] = forms.EmailInput(attrs=attrs)
            else:
                widgets[field] = forms.TextInput(attrs=attrs)
        # widgets = {
        #     "name": forms.Textnput(attrs={"class": "form-control"}),
        #     "address": forms.TextInput(attrs={"class": "form-control"}),
        #     "contact_person": forms.TextInput(attrs={"class": "form-control"}),
        #     "phone": forms.TextInput(attrs={"class": "form-control"}),
        #     "email": forms.EmailInput(attrs={"class": "form-control"}),
        # }
