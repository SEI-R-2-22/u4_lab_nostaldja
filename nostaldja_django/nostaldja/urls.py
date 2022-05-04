from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('fads/', views.fad_list, name='fad_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('fads/new', views.fad_create, name='fad_create'),
]
