from django.shortcuts import render, redirect
from .models import Decade
from .models import Fads
from .forms import DecadeForm, FadsForm
# Create your views here.


def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})


def fad_list(request):
    fads = Fads.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})


# def decade_create(request):
#     if request.method == '"POST":
#         form = DecadeForm(request.POST)
#         if form.is_valid():
#             decade = form.save()
#             return redirect('decade_detail', pk=decade.pk)

#         else:
#             form = DecadeForm()
#         return render(request, 'nostaldja/decade_form.html', {'form': form})


def fad_create(request):
    if request.method == "POST":
        form = FadsForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)

        else:
            form = FadsForm()
        return render(request, 'nostaldja/fad_form.html', {'form': form})


def decade_edit(request, pk):
    decade = Decade.objects.get(pk=pk)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)

        else:
            form = DecadeForm(instance=decade)
        return render(request, 'nostaldja/decade_form.html', {'form': form})


def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')


def fad_edit(request, pk):
    fad = Fads.objects.get(pk=pk)
    if request.method == "POST":
        form = FadsForm(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)

        else:
            form = FadsForm(instance=fad)
        return render(request, 'nostaldja/fad_form.html', {'form': form})


def fad_delete(request, pk):
    Fads.objects.get(id=pk).delete()
    return redirect('fad_list')
