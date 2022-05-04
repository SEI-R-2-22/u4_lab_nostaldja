from django.urls import path
from . import views

urlpatterns = [
    path('', views.fad_display_all, name='fad_display_all'),
    path('nostaldja_sub/detail/<int:pk>',
         views.fad_display_detail, name="fad_display_detail"),
    path('fad/new', views.fad_create, name='fad_create'),
    path('fad/<int:pk>/edit', views.fad_edit, name='fad_edit'),

    path('decade', views.decade_display_all, name='decade_display_all'),
    path('decade/detail/<int:pk>',
         views.decade_display_detail, name="decade_display_detail"),
    path('decade/new', views.decade_create, name='decade_create'),
    path('decade/<int:pk>/edit', views.decade_edit, name='decade_edit')
]
