from django.forms import forms
from .models import Worker


class CreateWorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "surname": forms.TextInput(attrs={"class": "form-control"}),
        }

class UpdateWorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "surname": forms.TextInput(attrs={"class": "form-control"}),
        }