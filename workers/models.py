import datetime

from django.db import models

from projects.models import Project


class Worker(models.Model):
    class Meta:
        ordering = ("surname",)

    name = models.CharField(max_length=50, unique=False)
    surname = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return f"{self.surname} {self.name}"


class WorkerForProject(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="workers")
    date = models.DateField(default=datetime.date.today)
    hours_amount = models.PositiveIntegerField(default=0)
    price_per_hour = models.FloatField(default=0, max_length=10)

    def __str__(self):
        return f"{self.worker}"
