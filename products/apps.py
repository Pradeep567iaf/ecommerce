from django.apps import AppConfig


class DepositConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    # def ready(self):
    #     from .signals import auto_load_name
