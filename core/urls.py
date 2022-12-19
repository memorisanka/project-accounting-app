from .views import HomeView
from django.urls import path, include

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]