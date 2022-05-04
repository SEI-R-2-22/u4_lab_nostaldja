from django.shortcuts import render
from .models import Fads, Decades

from .forms import DecadesForm, FadsForm
from django.shortcuts import render, redirect

# Create your views here.
def get_all_decades(request):
  decades = Decades.objects.all()
  return render(request, 'tunr/decades.html', {'decades': decades})

def decades_new(request):
  if request.method == 'POST':
    form = DecadesForm(request.POST)
    if form.is_valid():
      decades = form.save()
      return redirect('decades')
  else:
    form = DecadesForm()
  return render(request, 'tunr/decades_form.html', {'form': form})

def decades_edit(request, pk):
  decade = Decades.objects.get(pk=pk)
  if request.method == "POST":
    form = DecadesForm(request.POST, instance=decade)
    if form.is_valid():
      decade = form.save()
      return redirect('decades')
  else:
      form = DecadesForm(instance=decade)
  return render(request, 'tunr/decades_form.html', {'form': form})

def decades_delete(request, pk):
  Decades.objects.get(id=pk).delete()
  return redirect('decades')


def get_all_fads(request):
  fads = Fads.objects.all()
  return render(request, 'tunr/fads.html', {'fads': fads})

def fads_new(request):
  if request.method == 'POST':
    form = FadsForm(request.POST)
    if form.is_valid():
      fads = form.save()
      return redirect('fads')
  else:
    form = FadsForm()
  return render(request, 'tunr/fads_form.html', {'form': form})

def fads_edit(request, pk):
  fad = Fads.objects.get(pk=pk)
  if request.method == "POST":
    form = FadsForm(request.POST, instance=fad)
    if form.is_valid():
      fad = form.save()
      return redirect('fads')
  else:
      form = FadsForm(instance=fad)
  return render(request, 'tunr/fads_form.html', {'form': form})

def fads_delete(request, pk):
  Fads.objects.get(id=pk).delete()
  return redirect('fads')