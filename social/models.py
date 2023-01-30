from django.db import models

# Create your models here.
class Link(models.Model):
    # Este campo nos obliga a utilizar campos alfanumericos, guiones y barras, y no permitirá utilizar espacios ni caracteres especiales
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Nombre', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, blank=True, null=True)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)
    
    class Meta():
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['-name']
    
    def __str__(self):
        return self.name