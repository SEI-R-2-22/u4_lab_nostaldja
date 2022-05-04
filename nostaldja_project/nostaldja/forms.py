from django import forms
from .models import Decade, Fad

class DecadeForm(forms.ModelForm):

    class Meta:
        model = Decade
        fields = ('name', 'photo_url', 'nationality',)
    
class FadForm(forms.ModelForm):

    class Meta:
        model = Fad
        fields = ('name', 'image_url', 'description', 'decade', )