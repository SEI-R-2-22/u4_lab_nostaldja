from django.urls import path
from . import views

urlpatterns = [
  path('', views.decade_list, name='decade_list'),
  path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
  path('decades/new', views.decade_create, name='decade_create'),
  path('decades/<int:pk>/edit', views.decade_edit, name='decade_edit'),


  path('fads/', views.fad_list, name='fad_list'),
  path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
]