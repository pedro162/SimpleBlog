from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def posts_list(request, template_name="home.html"):
    posts = Postagem.objects.all()
    posts = {'list': posts}
    return render(request, template_name, posts)

def post_detail(request, pk, template_name='details.html'):
    post = get_object_or_404(Postagem, pk=pk)
    return render(request, template_name, {'post': post})