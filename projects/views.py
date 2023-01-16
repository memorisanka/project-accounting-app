from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from projects.models.client import Client
from projects.models.project import Project
from .forms import CreateClientForm, UpdateClientForm, CreateProjectForm


class ProjectListView(ListView):
    model = Project
    paginate_by = 12
    ordering = "name"

class CreateProjectView(CreateView):
    model = Project
    form_class = CreateProjectForm
    template_name = "create_project.html"

    def get_success_url(self):
        messages.success(self.request, "Pomyślnie zapisano projekt.")
        return reverse("detail-project", args=[self.object.id])

class DetailProjectView(DetailView):
    model = Project
    template_name = "detail_project.html"


class DeleteProjectView(DeleteView):
    model = Project
    template_name = "delete_project.html"

    def get_success_url(self):
        messages.success(self.request, "Projekt został pomyślnie usunięty.")
        return reverse("projects-list")

class CreateClientView(CreateView):
    model = Client
    form_class = CreateClientForm
    template_name = "create_client.html"

    def get_success_url(self):
        messages.success(self.request, "Klient pomyślnie zapisany.")
        return reverse("detail-client", args=[self.object.id])


class DetailClientView(DetailView):
    model = Client
    template_name = "detail_client.html"


class UpdateClientView(UpdateView):
    model = Client
    form_class = UpdateClientForm
    template_name = "update_client.html"

    def get_success_url(self):
        messages.success(self.request, "Dane klienta zostały uaktualnione.")
        return reverse("detail-client", args=[self.object.id])


class DeleteClientView(DeleteView):
    model = Client
    template_name = "delete_client.html"

    def get_success_url(self):
        messages.success(self.request, "Klient został pomyślnie usunięty.")
        return reverse("detail-client")



