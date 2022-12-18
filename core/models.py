from django.db import models


class Unit(models.Model):
    class Meta:
        ordering = ("name",)

    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"


class Worker(models.Model):
    class Meta:
        ordering = ("surname",)

    name = models.CharField(max_length=50, unique=False)
    surname = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return f"{self.surname} {self.name}"


class Service(models.Model):
    class Meta:
        ordering = ("name",)

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class SteelType(models.Model):
    class Meta:
        ordering = ("name",)

    steel_type = models.IntegerField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.steel_type}"


class Product(models.Model):
    class Meta:
        ordering = ("steel_type",)

    name = models.CharField(max_length=100, unique=True)
    unit = models.ForeignKey(Unit, max_length=10, on_delete=models.CASCADE)
    steel_type = models.ForeignKey(SteelType, max_length=10, on_delete=models.CASCADE)
