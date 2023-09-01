"""Models inventory"""

# Django 
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class StorageLocation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    location_id = models.ForeignKey(StorageLocation, on_delete=models.PROTECT)
    stock = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=10) # Nivel bajo de inventario
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class MovementInventory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=[('E', 'Entrada'), ('S', 'Salida')])
    amount = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_id


