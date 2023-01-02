from django.contrib import admin
from .models import Product, Project, Worker


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "unit", "steel_type", )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("name", )