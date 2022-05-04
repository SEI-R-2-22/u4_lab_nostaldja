from django.urls import path
from . import views

urlpatterns = [
    path('', views.fad_event, name='fad_event'),
]
