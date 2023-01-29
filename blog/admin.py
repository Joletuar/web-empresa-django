from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    # Especificamos las columnas que queremos mostrar en el panel de administrador
    list_display = ('title', 'author', 'published', 'post_categories')
    # Especificamos un lista de campos por las cuales queremos ordenar dentro del panel de administración
    ordering = ('author', 'published')
    # Crear un formulario de búsqueda
    search_fields = ('title','content','author__username','categories__name')
    # Permite implementar un forma más cómoda de navegar por fechas (jerarquizar)
    date_hierarchy = 'published'
    # Permite generar un panel de filtrado dentro del panel de administración
    list_filter = ('author__username','categories__name')
    
    # Podemos definir nuestros propios campos para mostrar
    
    def post_categories(self, obj):
        return ",".join([c.name for c in obj.categories.all().order_by("name")])
    
    # Cambiar el nombre de la nueva columna que hemos creado
    post_categories.short_description = "Categorías"

    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
