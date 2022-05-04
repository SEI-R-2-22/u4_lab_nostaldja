from django.shortcuts import render, redirect
from .forms import DecadeUpdateForm


from .models import Decade, Fads
# Create your views here.


def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})


def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})


def fad_list(request):
    fads = Fads.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})


def fad_detail(request, pk):
    fad = Fads.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})


def decade_update(request, pk):
    print("hit")
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
