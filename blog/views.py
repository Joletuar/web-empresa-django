from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {
        'posts': posts
    })

def category(request, category_id):
    # El get nos permite obtener un único registro en base a un parámetro de búsqueda
    #category = Category.objects.get(pk = category_id)
    category = get_object_or_404(Category, pk = category_id)
    return render(request, 'blog/category.html', {
        'category': category 
    })