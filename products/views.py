from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 12
    ordering = "name"


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "create_product.html"

    def get_success_url(self):
        messages.success(self.request, "Produkt pomyślnie zapisany.")
        return reverse("detail-product", args=[self.object.id])


class DetailProductView(DetailView):
    model = Product
    template_name = "detail_product.html"


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "update_product.html"

    def get_success_url(self):
        messages.success(self.request, "Produkt został uaktualniony.")
        return reverse("detail-product", args=[self.object.id])


class DeleteProductView(DeleteView):
    model = Product
    template_name = "delete_product.html"

    def get_success_url(self):
        messages.success(self.request, "Produkt został pomyślnie usunięty.")
        return reverse("detail-product")
