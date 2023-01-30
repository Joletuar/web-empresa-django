from django import template
from pages.models import Page

# Vamos a crear nuestro propio template tag para usarlo en todas nuestras páginas 

register = template.Library()

# Transformamos una función normal y lo registramos
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages

# Dentro de la página donde queramos utilizarlo tenemos que cargarlo usando:
# {% load page_extras %}