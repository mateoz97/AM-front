from django.apps import AppConfig


class ExtendedUiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.extended_ui"
