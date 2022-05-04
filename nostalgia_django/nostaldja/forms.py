# tunr/forms.py
from django import forms
from .models import Decade, Fads

class FadsForm(forms.ModelForm):

    class Meta:
        model = Fads
        fields = ('name', 'imageUrl', 'description', 'decade')
        
class DecadeForm(forms.ModelForm):

    class Meta:
        model = Decade
        fields = ('start_year')