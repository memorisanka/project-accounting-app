from django import forms
from projects.models.client import Client


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
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "contact_person": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
