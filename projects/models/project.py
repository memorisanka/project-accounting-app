import datetime
from django.db import models
from .client import Client
from .worker import WorkerWorkingTime
from .product import ProductCreate
from .service import ServiceCreate


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    date_create = models.DateTimeField(default=datetime.datetime.now(), blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    workers = models.ManyToManyField(WorkerWorkingTime, related_name='projects', blank=True)
    products = models.ManyToManyField(ProductCreate, related_name='projects', blank=True)
    services = models.ManyToManyField(ServiceCreate, related_name='projects', blank=True)
    finished = models.BooleanField(default=False)

    def get_workers(self):
        return ",".join([str(p) for p in self.workers.all()])

    def get_products(self):
        return ",".join([str(p) for p in self.products.all()])

    def get_services(self):
        return ",".join([str(p) for p in self.services.all()])

    def __str__(self):
        return f"{self.name}"