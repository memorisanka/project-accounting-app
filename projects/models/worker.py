from django.db import models

class Worker(models.Model):
    class Meta:
        ordering = ("surname",)

    name = models.CharField(max_length=50, unique=False)
    surname = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return f"{self.surname} {self.name}"
