from django.urls import path
from . import views

urls = [
    path('', views.decade_list, name='decade_list'),
    path('fads/', views.fad_list, name='fad_list'),
    path('decades/<int:pk>', views.decade_details, name='decade_details'),
    path('fads/<int:pk>', views.fad_detail, name='fad_details')
]