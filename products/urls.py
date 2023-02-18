from django.urls import path

from . import views

urlpatterns = [
    path('product/create/', views.CreateProductView.as_view(), name='create-product'),
    path('product/<int:pk>/', views.DetailProductsView.as_view(), name='detail-product'),
    path('product/<int:pk>/update/', views.UpdateProductView.as_view(), name='update-product'),
    path('product/<int:pk>/delete/', views.DeleteProductView.as_view(), name='delete-product'),
    path("product/list/", ProductListView.as_view(), name="products-list"),
]
