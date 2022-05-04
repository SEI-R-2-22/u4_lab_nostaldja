from django.shortcuts import render
from .models import Fad, Decade
# Create your views here.


def fad_event(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja_sub/fad_event.html', {'fads': fads})
