from django.shortcuts import render, redirect
from .models import Fad, Decade
from .forms import FadForm, DecadeForm

# Create your views here.


def fad_display_all(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja_sub/fad_display_all.html', {'fads': fads})


def fad_display_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja_sub/fad_display_detail.html', {'fad': fad})


def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_display_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'nostaldja_sub/fad_form.html', {'form': form})


def fad_edit(request, pk):
    fad = Fad.objects.get(pk=pk)
    if request.method == "POST":
        form = Fad(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_display_detail', pk=fad.pk)
    else:
        form = FadForm(instance=fad)
    return render(request, 'nostaldja_sub/fad_form.html', {'form': form})


def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_display_all')


def decade_display_all(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja_sub/decade_display_all.html', {'decades': decades})


def decade_display_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja_sub/decade_display_detail.html', {'decade': decade})


def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_display_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostaldja_sub/decade_form.html', {'form': form})


def decade_edit(request, pk):
    decade = Decade.objects.get(pk=pk)
    if request.method == "POST":
        form = Decade(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_display_detail', pk=decade.pk)
    else:
        form = FadForm(instance=decade)
    return render(request, 'nostaldja_sub/decade_form.html', {'form': form})


def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_display_all')
