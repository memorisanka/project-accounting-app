from django.db import models

from projects.models import Project


class SteelType(models.TextChoices):
    STEEL_1 = "304", "304"
    STEEL_2 = "316", "316"
    STEEL_3 = "321", "321"


class UnitType(models.TextChoices):
    kg = "kg", "kg"
    mb = "mb", "mb"
    piece = "szt.", "szt."


class Product(models.Model):
    class Meta:
        ordering = ("name",)

    name = models.CharField(max_length=100, unique=True, verbose_name='Nazwa produktu')
    unit = models.CharField(
        max_length=10, choices=UnitType.choices, help_text="jednostka", verbose_name='Jednostka'
    )
    steel_type = models.CharField(choices=SteelType.choices, max_length=10, verbose_name='Gatunek stali')
    description = models.CharField(max_length=255, blank=True, verbose_name='Opis / uwagi')

    def __str__(self):
        return f"{self.name} {self.steel_type}"


class ProductForProject(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, verbose_name='Wybierz produkt')
    amount = models.FloatField(default=0, max_length=10, verbose_name='Ilość')
    price = models.FloatField(default=0, max_length=10, verbose_name='Cena')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Wybierz projekt')

    def __str__(self):
        return f"{self.product}"
