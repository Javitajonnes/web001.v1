from django.contrib import admin
from django.urls import path
from core import views as views_core
from posteo import views as views_posteo

urlpatterns = [
    
    path('',views_core.home,name="home"),
    path('noticias/',views_posteo.noticia, name="noticias"),
    path('admin/', admin.site.urls),
    
]
