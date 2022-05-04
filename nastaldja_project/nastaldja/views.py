from django.shortcuts import render
from .models import Decade, Fads

# Create your views here.


def decade_list(request):
    decade = Decade.objects.all()
    return render(request, 'nastaldja/decade_list.html', {'decades': decade})
