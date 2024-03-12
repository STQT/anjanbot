from datetime import datetime

from django.db import models

from app.address.models import Branch
from app.users.models import TelegramUser
from django.utils.translation import gettext_lazy as _


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


class Order(models.Model):
    class STATUS(models.TextChoices):
        CREATED = ("created", _("Yaratildi"))
        PROCEED = ("proceed", _("Ko'rib chiqildi"))

    comment = models.TextField(blank=True, null=True)
    cash_type = models.CharField(max_length=10)
    delivery = models.CharField(max_length=3)
    address = models.CharField(max_length=500, null=True, blank=True)
    filial = models.ForeignKey(Branch, on_delete=models.CASCADE)
    distance = models.CharField(max_length=10, null=True, blank=True)
    cost = models.CharField(max_length=10)
    delivery_cost = models.CharField(max_length=10)
    all_cost = models.CharField(max_length=10)
    user = models.ForeignKey(TelegramUser, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS.choices, default=STATUS.CREATED)
