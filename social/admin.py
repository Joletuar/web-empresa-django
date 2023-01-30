from django.contrib import admin
from .models import *

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
    # Vamos a extender para modificar ciertos parámetros en tiempo de ejecución
    def get_readonly_fields(self,request, objt=None):
        if request.user.groups.filter(name='Personal').exists():
            return ['key', 'name']
        else:
            return ['created', 'updated']
            

admin.site.register(Link, LinkAdmin)