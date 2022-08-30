from django.shortcuts import render

# Create your views here.
from .models import Decade,Fad

def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html',{'decades':decades})

def fad_list(request):
    fad = Fad.objects.all()
    return render(request,'nostaldja/fad_list.html',{'fad':fad})

def decade_detail(request, pk):
    dec = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html',{'decade':dec})

def fad_detail(request,pk):
    fads = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html',{'fads':fads})