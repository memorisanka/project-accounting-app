from django.views.generic.list import ListView
from .models import Product



class ProductListView(ListView):
    model = Product
    paginate_by = 10
