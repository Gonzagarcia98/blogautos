from django import forms
from .models import Auto, Categoria, Reseña

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año', 'descripcion', 'imagen', 'categorias']

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['auto', 'titulo', 'contenido']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']