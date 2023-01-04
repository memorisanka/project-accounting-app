from django.db import models
from .client import Client
from .worker import WorkerWorkingTime
from .product import ProductCreate
from .service import ServiceCreate


class Project(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    workers = models.ManyToManyField(WorkerWorkingTime, related_name='projects')
    products = models.ManyToManyField(ProductCreate, related_name='projects')
    services = models.ManyToManyField(ServiceCreate, related_name='projects')

    def get_workers(self):
        return ",".join([str(p) for p in self.workers.all()])

    def get_products(self):
        return ",".join([str(p) for p in self.products.all()])

    def get_services(self):
        return ",".join([str(p) for p in self.services.all()])