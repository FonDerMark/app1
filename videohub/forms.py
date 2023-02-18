from django import forms
from .models import Films


class FilmsForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = '__all__'
