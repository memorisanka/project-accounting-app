from django.urls import path

from . import views

urlpatterns = [
    path('worker/<int:pk>/', views.DetailWorkerView.as_view(), name='detail-worker'),
    path('worker/create/', views.CreateWorkerView.as_view(), name='create-worker'),
    # path('worker/<int:pk>/update/', views.UpdateClientView.as_view(), name='update-client'),
    # path('worker/<int:pk>/delete/', views.DeleteClientView.as_view(), name='delete-client'),
    # path("worker/list/", ClientListView.as_view(), name="clients-list"),
]
