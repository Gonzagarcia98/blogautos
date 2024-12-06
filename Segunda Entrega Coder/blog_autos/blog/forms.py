from django import forms
from .models import Auto, Reseña, Categoria

from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año', 'descripcion', 'imagen']

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['auto', 'titulo', 'contenido']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'autos']