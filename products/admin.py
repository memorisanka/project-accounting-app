from django.contrib import admin

from .models import Product, ProductForProject


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "unit",
        "steel_type",
    )


@admin.register(ProductForProject)
class ProductForProjectAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "amount",
        "price",
        "project",
    )
