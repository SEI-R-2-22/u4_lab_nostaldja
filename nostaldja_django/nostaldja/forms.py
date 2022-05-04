from django import forms
from .models import Decade, Fads


class DecadeUpdateForm(forms.ModelForm):

    class Meta:
        model = Decade
        fields = ('start_year',)
