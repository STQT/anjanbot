from datetime import datetime

from django.db import models


def upload_path(instance, filename):
    today = datetime.now()
    return '{0}/{1}/{2}/{3}'.format(
        today.year,
        today.strftime('%m'),
        today.strftime('%d'),
        filename
    )


class Category(models.Model):
    name = models.CharField(verbose_name="Nomi", max_length=100)
    image = models.ImageField(verbose_name="Rasmi", upload_to=upload_path, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активный?", default=False)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="Nomi", max_length=100)
    price = models.IntegerField(verbose_name="Narxi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(verbose_name="Rasmi", upload_to=upload_path, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активный?", default=False)

    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"

    def __str__(self):
        return self.name
