from django.urls import path

from . import views

urlpatterns = [
    path('decades/', views.decade_list, name='decade_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/', views.fad_list, name='fad_list'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail')
]
