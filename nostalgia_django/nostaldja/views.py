from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import FadsForm, DecadeForm

# Create your views here.
def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})

def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})

def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')


def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fads_list.html', {'fads': fads})

def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fads_detail.html', {'fad': fad})

def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')



def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'nostaldja/fads_form.html', {'form': form})


def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'nostaldja/decade_form.html', {'form': form})

def fad_edit(request, pk):
    fads = FadsForm().objects.get(pk=pk)
    if request.method == "POST":
        form = FadsForm(request.POST, instance=fads)
        if form.is_valid():
            fads = form.save()
            return redirect('fads_detail', pk=fads.pk)
    else:
        form = FadsForm(instance=artist)
    return render(request, 'nostaldja/fads_form.html', {'form': form})

def decade_edit(request, pk):
    decade = Decade().objects.get(pk=pk)
    if request.method == "POST":
        form = DeacdeForm(request.POST, instance=decade)
        if form.is_valid():
            deacde = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'nostaldja/decade_form.html', {'form': form})