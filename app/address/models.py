from ckeditor.fields import RichTextField
from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        verbose_name = "Manzil"
        verbose_name_plural = "Manzillar"

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(max_length=1023, null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    is_active = models.BooleanField(verbose_name="Faolmi?", default=False)

    class Meta:
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"

    def __str__(self):
        return self.name
