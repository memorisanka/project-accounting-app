from django.db import models


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


class SteelType(models.TextChoices):
    STEEL_1 = '304', '304'
    STEEL_2 = '316', '316'
    STEEL_3 = '321', '321'

class UnitType(models.TextChoices):
    kg = 'kg', 'kg'
    mb = 'mb', 'mb'
    piece = 'szt.', 'szt.'


class Product(models.Model):
    class Meta:
        ordering = ("name",)

    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=10, choices=UnitType.choices, help_text="jednostka")
    amount = models.FloatField(default=0, null=True)
    steel_type = models.CharField(choices=SteelType.choices, max_length=10)
