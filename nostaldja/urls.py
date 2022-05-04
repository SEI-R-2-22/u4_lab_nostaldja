from django.urls import path

from . import views

urlpatterns = [
    path('decades/', views.decade_list, name='decade_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/', views.fad_list, name='fad_list'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('decade/update/<int:pk>', views.decade_update, name='decade_update'),
    path('fad/update/<int:pk>', views.fad_update, name='fad_update'),
    path('decade/create/', views.decade_create, name='decade_create'),
    path('fad/create/', views.fad_create, name='fad_create'),
    path('decade/delete/<int:pk>', views.decade_delete, name='decade_delete'),
    path('fad/delete/<int:pk>', views.fad_delete, name='fad_delete')
]
