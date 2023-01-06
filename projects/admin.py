from django.contrib import admin
from .models import Project, Client
from projects.models.product import Product, ProductCreate
from projects.models.service import Service, ServiceCreate
from projects.models.worker import Worker, WorkerWorkingTime


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
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_create",
        "client",
        "get_workers",
        "get_products",
        "get_services",
        "ended",
    )


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
    )


@admin.register(WorkerWorkingTime)
class WorkerWorkingTimeAdmin(admin.ModelAdmin):
    list_display = ("worker", "date", "hours_amount", "price_per_hour")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "contact_person",
        "phone",
        "email",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ServiceCreate)
class ServiceCreateAdmin(admin.ModelAdmin):
    list_display = ("service", "amount", "price")
