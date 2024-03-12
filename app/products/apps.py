from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.products"

    def ready(self):
        try:
            import app.products.signals  # noqa: F401
        except ImportError:
            print("HEE")
