from django.contrib import admin

from .models import Product, ProductCreate


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "unit",
        "steel_type",
    )


@admin.register(ProductCreate)
class ProductCreateAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "amount",
        "price",
        "project",
    )
