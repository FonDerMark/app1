from django import forms
from .models import CryptoFile


class CGForm(forms.ModelForm):
    class Meta:
        model = CryptoFile
        fields = '__all__'
        widgets = {
            'encoded': forms.HiddenInput(),
        }
