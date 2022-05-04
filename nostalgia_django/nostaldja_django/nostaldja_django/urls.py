"""nostaldja_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
    path('', views.name, name='name'),
    path('decades/', views.decade_list, name="decade_list"),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('decades/<int:pk>/edit', views.decades_edit, name='decade_edit'),
    path('decdes/<int:pk>/delete', views.decades_delete, name='decade_delete'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('fads/', views.fad_list, name='fad_list'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('fads/new', views.fad_create, name='fad_create'),
    path('fads/<int:pk>/edit', views.fad_edit, name='fad_edit'),
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete')
]