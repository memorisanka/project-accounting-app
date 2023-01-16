from django.urls import path
from . import views
from .views import ProjectListView

urlpatterns = [
    # path('search/', views.SearchResultsView.as_view(), name='search'),
    path('client/create/', views.CreateClientView.as_view(), name='create-client'),
    path('client/<int:pk>/', views.DetailClientView.as_view(), name='detail-client'),
    path('client/<int:pk>/update/', views.UpdateClientView.as_view(), name='update-client'),
    path('client/<int:pk>/delete/', views.DeleteClientView.as_view(), name='delete-client'),
    path('project/create/', views.CreateProjectView.as_view(), name='create-project'),
    path('project/<int:pk>/', views.DetailProjectView.as_view(), name='detail-project'),
    path("project/projects_list/", ProjectListView.as_view(), name="projects-list"),
    path('project/<int:pk>/delete/', views.DeleteProjectView.as_view(), name='delete-project'),
]
