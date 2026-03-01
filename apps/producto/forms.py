import django.forms as forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # Agregamos serie_retirada y fecha_salida (opcional)
        fields = [
            'marca', 
            'modelo', 
            'serie', 
            'estado', 
            'serie_retirada', 
            'fecha_salida', 
            'observaciones'
        ]
        
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Huawei'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: HG8245H'}),
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'serie_retirada': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Solo si es un cambio'}),
            # Un selector de fecha para la salida
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }