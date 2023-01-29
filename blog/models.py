from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User # Contiene todos los modelos de los usuarios registrados en el panel de administración

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta():
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name = 'Contenido')
    # Se especfica un valor por defecto que sea la hora y fecha actual del proyecto
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(upload_to='blog', verbose_name='Imagen', null=True, blank=True)
    # Relacionamos un post con un autor / Relación de uno a uno
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    # Relación de muchos a muchos
    # related_name permite definir el nombre de un método que permitirá obtener los objetos que se relacionen con la categoría, es decir, una busqueda de relación inversa
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta():
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']
    
    def __str__(self):
        return self.title