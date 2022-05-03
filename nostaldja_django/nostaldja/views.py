from django.shortcuts import render

from .models import Decade, Fad
# Create your views here.


def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})
