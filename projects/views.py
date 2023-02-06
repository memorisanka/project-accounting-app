from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project
from workers.models import Worker
from .forms import ProjectForm, ProjectForm


class HomeView(TemplateView):
    template_name = "home.html"


class ProjectListView(ListView):
    model = Project
    paginate_by = 12
    ordering = "name"


class CRUDView(View):
    model = None
    form_class = None
    template_name = None


class OwnCreateView(CRUDView, CreateView):
    pass


# class CreateProjectView(OwnCreateView):
#     model = Project
#     form_class = CreateProjectForm
#     template_name = "create_project.html"
#     success_message = 'Project successfully saved.'
#     success_url = reverse('detail-project', args=[Project.pk])

class BaseProjectView:
    model = Project

    success_message = None
    success_url = None

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url


class CreateProjectView(BaseProjectView, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "create_project.html"

    def get_success_url(self):
        messages.success(self.request, "Pomyślnie zapisano projekt.")
        return reverse("detail-project", args=[self.object.id])


class DetailProjectView(DetailView):
    model = Project
    template_name = "detail_project.html"

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['workers'] = Worker.objects.all()
    #     return data


class UpdateProjectView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "update_project.html"

    def get_success_url(self):
        messages.success(self.request, "Dane klienta zostały uaktualnione.")
        return reverse("detail-client", args=[self.object.id])


class DeleteProjectView(DeleteView):
    model = Project
    template_name = "delete_project.html"

    def get_success_url(self):
        messages.success(self.request, "Projekt został pomyślnie usunięty.")
        return reverse("projects-list")
