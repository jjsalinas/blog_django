from django import forms

from .models import Entrada

class FormEntrada(forms.ModelForm):
    
    class Meta:
        model = Entrada
        fields = ('titulo', 'cuerpo',)