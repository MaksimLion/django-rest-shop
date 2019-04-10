from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория продуктов"
        verbose_name_plural = "Категории продуктов"


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    category = models.ForeignKey(to=ProductCategory, verbose_name="Категория", on_delete=models.CASCADE)
    cost = models.IntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    in_stock = models.BooleanField(default=False)
    count = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


# class Order(models.Model):
#     owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(to=Product)
#     cost = models.IntegerField()

