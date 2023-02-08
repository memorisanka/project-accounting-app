from django import forms
from .models import Worker


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "surname": forms.TextInput(attrs={"class": "form-control"}),
        }
