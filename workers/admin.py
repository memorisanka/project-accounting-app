from django.contrib import admin

from .models import Worker, WorkerForProject


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
    )


@admin.register(WorkerForProject)
class WorkerForProjectAdmin(admin.ModelAdmin):
    list_display = ("worker", "date", "hours_amount", "price_per_hour", "project")
