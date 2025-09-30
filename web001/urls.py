from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views as views_core
from posteo import views as views_posteo

urlpatterns = [
    
    path('',views_core.home,name="home"),
    path('noticias/',views_posteo.noticia, name="noticias"),
    path('admin/', admin.site.urls),
    
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
