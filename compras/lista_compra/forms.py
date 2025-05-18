from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['producto', 'precio', 'establecimiento']
        widgets = {
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',  # permite decimales
                'min': '0'
            }),
            'establecimiento': forms.Select(attrs={'class': 'form-select'}),
        }