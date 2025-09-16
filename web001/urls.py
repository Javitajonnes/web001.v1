from django.contrib import admin
from django.urls import path
from core import views as views_core

urlpatterns = [
    
    path('',views_core.home,name="home"),
    path('admin/', admin.site.urls),
    
]
