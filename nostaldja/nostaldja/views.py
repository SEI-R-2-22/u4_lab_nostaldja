from django.shortcuts import render
from .models import Decade, Fad

def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})

def decade_details(request):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nstaldja/decade_list.html', {'decade': decade})

def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})

def fad_details(request):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})