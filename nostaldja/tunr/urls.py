from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_all_decades, name='decades'),
  path('decades/new', views.decades_new, name='decades_new'),
  path('decades/<int:pk>/edit', views.decades_edit, name='decades_edit'),
  path('decades/<int:pk>/delete', views.decades_delete, name='decades_delete'),
  path('fads/', views.get_all_fads, name='fads'),
  path('fads/new', views.fads_new, name='fads_new'),
  path('fads/<int:pk>/edit', views.fads_edit, name='fads_edit'),
  path('fads/<int:pk>/delete', views.fads_delete, name='fads_delete')
]