from django.db import models
from ckeditor.fields import RichTextField # Importamos el componente que va a sustituir el componente normal


# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Título', max_length=200)
    # Vamos a sustituir este contenido plano por el editor que instalamos
    # content = models.TextField(verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido')
    # Entero pequeño
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)
    
    class Meta():
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title