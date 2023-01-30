# El contexto corresponde a una serie de parámetros que por defecto ya todos los templates de django tienen. Por ejemplo, se puede acceder a la variable request.path sin la necesidad de pasarle a la vista dicha variable

# Vamos a extender dicho contexto para incluir nuevos variables

# Esto de aqui se extiende dentro del archivo settings.py en el apartado TEMPLATE

from .models import *

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url 
    return ctx