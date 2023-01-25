from django.contrib import admin
from .models import Service, ServiceCreate


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ServiceCreate)
class ServiceCreateAdmin(admin.ModelAdmin):
    list_display = ("service", "amount", "price", "project")