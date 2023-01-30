from django.apps import AppConfig


class PagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pages"
    # Permite cambiar el nombre de como se mostrará esta sección en el panel de administración
    verbose_name = 'Gestor de Páginas'
