'''
forms
'''
from .models import Decade, Fads
from django import forms


class DecadeForm(forms.ModelForm):
    class Meta:
        model = Decade
        fields = ('start_year',)


class FadsForm(forms.ModelForm):
    class Meta:
        model = Fads
        fields = ('decade', 'name', 'image_url', 'description',)
