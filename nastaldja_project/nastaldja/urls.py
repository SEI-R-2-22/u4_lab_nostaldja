
from django.urls import path
from . import views

urlpatterns = [
    path('decade/', views.decade_list, name='decade_list')
]
