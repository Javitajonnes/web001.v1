from django.shortcuts import render
from .models import Noticia

def noticia(request):
    noticia=Noticia.objects.all() # devuelve lista de noticias desde BD
    return render(request,"posteo/noticias.html",{"noticia":noticia})
