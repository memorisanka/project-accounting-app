from django.db import models


class Service(models.Model):
    class Meta:
        ordering = ("name",)

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

class ServiceCreate(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)
    amount = models.FloatField(default=0, max_length=10)
    price = models.FloatField(default=0, max_length=10)
