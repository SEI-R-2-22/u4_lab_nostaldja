from django.contrib import admin

# Register your models here.
from .models import Decade, Fads

admin.site.register(Decade)
admin.site.register(Fads)