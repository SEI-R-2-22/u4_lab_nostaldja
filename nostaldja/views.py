from django.shortcuts import render, redirect

from .models import Decade, Fad
from .forms import DecadeUpdateForm, FadUpdateForm, DecadeForm, FadForm
# Create your views here.


def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})


def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})


def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})


def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})


def decade_update(request, pk):
    if request.method == 'POST':
        form = DecadeUpdateForm(request.POST)
        if form.is_valid():
            start_year = form.cleaned_data["start_year"]
            decade = Decade(id=pk, start_year=start_year)
            decade.save()
            return redirect(decade_detail, pk=decade.pk)
    else:
        form = DecadeUpdateForm()
    return render(request, "nostaldja/decade_update.html", {'form': form})


def fad_update(request, pk):
    if request.method == 'POST':
        form = FadUpdateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            image_url = form.cleaned_data["image_url"]
            description = form.cleaned_data["description"]
            fad = Decade(id=pk, name=name, image_url=image_url,
                         description=description)
            fad.save()
            return redirect(fad_detail, pk=fad.pk)
    else:
        form = FadUpdateForm()
    return render(request, "nostaldja/decade_update.html", {'form': form})


def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostaldja/decade_create.html', {'form': form})


def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'nostaldja/fad_create.html', {'form': form})


def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')


def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')
