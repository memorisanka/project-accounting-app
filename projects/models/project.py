from django.db import models
from .client import Client
from .worker import Worker


class Project(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    workers = models.ManyToManyField(Worker, related_name='projects')