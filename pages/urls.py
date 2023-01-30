from django.urls import path
from .views import page

urlpatterns = [
    # Slug: permite formatear de una forma mas bonita la url, trasnformando los espacios por guiones y poniendo todo en minusculas
    path('<int:page_id>/<slug:page_slug>/', page, name = 'sample_page'),
]