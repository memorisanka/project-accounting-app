from django.contrib import admin
from projects.models.product import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "unit", "steel_type")
