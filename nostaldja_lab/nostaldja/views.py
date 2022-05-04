from django.shortcuts import render
from .models import Decade, Fads
# Create your views here.
def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})

def fads_list(request):
    fads = Fads.objects.all()
    return render(request, 'nostaldja/fads_list.html', {'fads': fads})

def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})

def fads_detail(request, pk):
    fad = Fads.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})