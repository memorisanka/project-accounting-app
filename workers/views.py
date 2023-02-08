from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import WorkerForm
from .models import Worker


class WorkerListView(ListView):
    model = Worker
    paginate_by = 12
    ordering = "surname"


class DetailWorkerView(DetailView):
    model = Worker
    template_name = "detail_worker.html"


class CreateWorkerView(CreateView):
    model = Worker
    form_class = WorkerForm
    template_name = "create_worker.html"

    def get_success_url(self):
        messages.success(self.request, "Pracownik pomyślnie zapisany.")
        return reverse("detail-worker", args=[self.object.id])
