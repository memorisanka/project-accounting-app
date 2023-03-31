from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from .forms import CreateClientForm, UpdateClientForm
from .models import Client


class ClientListView(ListView):
    model = Client
    paginate_by = 12
    ordering = "name"


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
