"""
URL configuration for blog_autos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auto/nuevo/', views.auto_nuevo, name='auto_nuevo'),
    path('reseña/nueva/', views.reseña_nueva, name='reseña_nueva'),
    path('categoria/nueva/', views.categoria_nueva, name='categoria_nueva'),
    path('buscar/', views.buscar, name='buscar'),
    path('auto/editar/<int:pk>/', views.auto_editar, name='auto_editar'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
]