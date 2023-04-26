from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from projects.models import Project
from .forms import ProjectForm


class HomeView(TemplateView):
    template_name = "home.html"


class ProjectListView(ListView):
    queryset = Project.objects.select_related("client")
    # model = Project
    paginate_by = 12
    ordering = "-date_create"


class CreateProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/create_project.html"

    def get_success_url(self):
        messages.success(self.request, "Pomyślnie zapisano projekt.")
        return reverse("detail-project", args=[self.object.id])


class DetailProjectView(DetailView):
    model = Project
    template_name = "projects/detail_project.html"

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['workers'] = Worker.objects.all()
    #     return data


class UpdateProjectView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/update_project.html"

    def get_success_url(self):
        messages.success(self.request, "Dane klienta zostały uaktualnione.")
        return reverse("detail-client", args=[self.object.id])


class DeleteProjectView(DeleteView):
    model = Project
    template_name = "projects/delete_project.html"

    def get_success_url(self):
        messages.success(self.request, "Projekt został pomyślnie usunięty.")
        return reverse("projects-list")
