from django.urls import path

from . import views
from .views import ProjectListView

urlpatterns = [
    # path('search/', views.SearchResultsView.as_view(), name='search'),
    path('create/', views.CreateProjectView.as_view(), name='create-project'),
    path('<int:pk>/', views.DetailProjectView.as_view(), name='detail-project'),
    path("list/", ProjectListView.as_view(), name="projects-list"),
    path('<int:pk>/delete/', views.DeleteProjectView.as_view(), name='delete-project'),
    path('<int:pk>/update/', views.UpdateProjectView.as_view(), name='update-project'),
]
