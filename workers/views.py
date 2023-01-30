from django.shortcuts import render
from django.views.generic import ListView, DetailView
from workers.models import Worker


class WorkerListView(ListView):
    model = Worker
    paginate_by = 12
    ordering = "surname"


class DetailWorkerView(DetailView):
    model = Worker
    template_name = "detail_worker.html"

