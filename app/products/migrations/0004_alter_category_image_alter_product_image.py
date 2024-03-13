# Generated by Django 4.2.9 on 2024-03-13 07:34

import app.products.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_order_charge_id_alter_order_cash_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=imagekit.models.fields.ProcessedImageField(
                blank=True, null=True, upload_to=app.products.models.upload_path, verbose_name="Rasmi"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=imagekit.models.fields.ProcessedImageField(
                blank=True, null=True, upload_to=app.products.models.upload_path, verbose_name="Rasmi"
            ),
        ),
    ]