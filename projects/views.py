from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from projects.models.client import Client
from .forms import CreateClientForm, UpdateClientForm


class CreateClientView(CreateView):
    model = Client
    form_class = CreateClientForm
    template_name = "create_client.html"

    def get_success_url(self):
        messages.success(self.request, "Client created.")
        return reverse("detail-client", args=[self.object.id])


class DetailClientView(DetailView):
    model = Client
    template_name = "detail_client.html"


class UpdateClientView(UpdateView):
    model = Client
    form_class = UpdateClientForm
    template_name = "update_client.html"

    def get_success_url(self):
        messages.success(self.request, "Client updated.")
        return reverse("detail-client", args=[self.object.id])


class DeleteClientView(DeleteView):
    model = Client
    template_name = "delete_client.html"

    def get_success_url(self):
        messages.success(self.request, "Client deleted.")
        return reverse("home")
