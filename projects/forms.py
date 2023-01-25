from django import forms

from projects.models import Project
from workers.models import Worker


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "date_create": forms.DateInput(attrs={"class": "form-control"}),
        }


class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "date_create": forms.DateInput(attrs={"class": "form-control"}),
        }

