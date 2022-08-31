from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Decades, Fads
admin.site.register(Decades)
admin.site.register(Fads)
