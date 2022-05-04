from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('fads/', views.fads_list, name='fads_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fads_detail, name='fads_detail')
]