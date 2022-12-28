from django import forms
from .models import CryptoFile

class CGForm(forms.ModelForm):
    class Meta:
        model = CryptoFile
        fields = ['file']