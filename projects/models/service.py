from django.db import models


class Service(models.Model):
    class Meta:
        ordering = ("name",)

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"
