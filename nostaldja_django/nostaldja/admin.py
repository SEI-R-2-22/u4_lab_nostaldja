from django.contrib import admin

# Register your models here.

from .models import Fad, Decade

admin.site.register(Fad)
admin.site.register(Decade)