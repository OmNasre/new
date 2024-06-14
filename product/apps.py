# from django.apps import AppConfig


# class ProductConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'product'


# apps.py
from django.apps import AppConfig

class ProductConfig(AppConfig):
    name = 'product'  # Replace with your actual app name

    def ready(self):
        import product.signals  # This ensures signals.py is imported
