from django.urls import path

from . import views

urlpatterns = [
    path('worker/<int:pk>/', views.DetailWorkerView.as_view(), name='detail-worker'),
]
