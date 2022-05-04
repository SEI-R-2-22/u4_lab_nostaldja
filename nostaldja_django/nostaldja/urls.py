from django.urls import path
from .import views

urlpatterns = [
    path('decades/', views.decade_list, name='decade_list'),
    path('decade/<int:pk>', views.decade_detail, name='decade_detail'),
    # path(), create decade
    # path(), update decade
    # path(), delete decade

    path('fads/', views.fad_list, name='fad_list'),
    path('fad/<int:pk>', views.fad_detail, name='fad_detail'),
    # path(), create fad
    # path(), update fad
    # path(), delete fad
] 