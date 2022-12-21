from django.urls import path, reverse_lazy
from .views import ProductListView


urlpatterns = [
    path("product/list", ProductListView.as_view(), name="product-list"),
]
