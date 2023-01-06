import datetime

from django.db import models


class Worker(models.Model):
    class Meta:
        ordering = ("surname",)

    name = models.CharField(max_length=50, unique=False)
    surname = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return f"{self.surname} {self.name}"


class WorkerWorkingTime(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=datetime.datetime.now())
    hours_amount = models.PositiveIntegerField(default=0)
    price_per_hour = models.FloatField(default=0, max_length=10)
