from django.contrib import admin
from .models import Product, Project, Worker, Client


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "amount",
        "unit",
        "steel_type",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
    )

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "contact_person",
        "phone",
        "email",
    )
