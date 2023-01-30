import datetime

from django.db.models import Sum

from clients.models import Client
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    date_create = models.DateTimeField(default=datetime.datetime.now(), blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_workers(self):
        return self.workers.all()

    def get_workers_summary(self):
        queryset = self.get_workers()
        return queryset.aggregate(total_hours=Sum("hours_amount"),
                                  total_price=Sum("price_per_hour"))