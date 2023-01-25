from django.urls import path

from . import views
from .views import HomeView
from .views import ProjectListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('search/', views.SearchResultsView.as_view(), name='search'),
    path('project/create/', views.CreateProjectView.as_view(), name='create-project'),
    path('project/<int:pk>/', views.DetailProjectView.as_view(), name='detail-project'),
    path("project/projects_list/", ProjectListView.as_view(), name="projects-list"),
    path('project/<int:pk>/delete/', views.DeleteProjectView.as_view(), name='delete-project'),
    path('project/<int:pk>/update/', views.UpdateProjectView.as_view(), name='update-project'),
]
