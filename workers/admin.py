from django.contrib import admin

from .models import Worker, WorkerWorkingTime


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
    )


@admin.register(WorkerWorkingTime)
class WorkerWorkingTimeAdmin(admin.ModelAdmin):
    list_display = ("worker", "date", "hours_amount", "price_per_hour", "project")
