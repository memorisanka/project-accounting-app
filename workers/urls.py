from django.urls import path

from . import views
from .views import WorkerListView

urlpatterns = [
    path('worker/<int:pk>/', views.DetailWorkerView.as_view(), name='detail-worker'),
    path('worker/create/', views.CreateWorkerView.as_view(), name='create-worker'),
    path('worker/list/', WorkerListView.as_view(), name="workers-list"),
    path('worker/<int:pk>/update/', views.UpdateWorkerView.as_view(), name='update-worker'),
    path('worker/<int:pk>/delete/', views.DeleteWorkerView.as_view(), name='delete-worker'),
]
