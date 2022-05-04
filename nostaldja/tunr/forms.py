# tunr/forms.py
from django import forms
from .models import Fads, Decades

class FadsForm(forms.ModelForm):
    class Meta:
        model = Fads
        fields = ('name', 'image_url', 'description',)

class DecadesForm(forms.ModelForm):
  class Meta:
    model = Decades
    fields = ('start_year',)