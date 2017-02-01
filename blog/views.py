from django.shortcuts import render

from .models import Post #Ahora tenemos que incluir el modelo que definimos en el archivo models.py
from django.utils import timezone

from django.shortcuts import get_object_or_404

# Create your views here.
#def post_list(request):
#	return render(request, 'blog/post_list.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

"""
	Observa que creamos una variable en nuestro QuerySet: posts. 
	Tómala como el nombre de nuestro QuerySet. 
	De aquí en adelante vamos a referirnos al QuerySet con ese nombre.

	
	El último parámetro, que se ve así: 
	{} es un campo en el que podemos agregar algunas cosas para que 
	la plantilla las use. Necesitamos nombrarlos 
	(los seguiremos llamando 'posts' por ahora :))
"""

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

