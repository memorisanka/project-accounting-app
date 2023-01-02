from django.db import models
from .worker import Worker


class Project(models.Model):
    name = models.CharField(max_length=50)
    workers = models.ManyToManyField(Worker, related_name='projects')