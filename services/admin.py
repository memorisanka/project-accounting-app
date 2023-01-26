from django.contrib import admin
from .models import Service, ServiceForProject


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ServiceForProject)
class ServiceForProjectAdmin(admin.ModelAdmin):
    list_display = ("service", "amount", "price", "project")