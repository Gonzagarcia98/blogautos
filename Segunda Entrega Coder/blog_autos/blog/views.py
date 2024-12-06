from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Auto, Reseña, Categoria
from django.db.models import Q
from .forms import AutoForm, ReseñaForm, CategoriaForm
from django.shortcuts import render, redirect, get_object_or_404

def auto_editar(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == "POST":
        form = AutoForm(request.POST, request.FILES, instance=auto)
        if form.is_valid():
            if 'imagen' in request.FILES:
                auto.imagen = request.FILES['imagen']
            auto = form.save()
            return redirect('home')
    else:
        form = AutoForm(instance=auto)
    return render(request, 'blog/auto_form.html', {'form': form, 'editing': True})

def home(request):
    autos = Auto.objects.all()
    for auto in autos:
        print(f"Auto: {auto}")
        print(f"Tiene imagen: {bool(auto.imagen)}")
        if auto.imagen:
            print(f"Ruta de imagen: {auto.imagen.url}")
    return render(request, 'blog/home.html', {'autos': autos})

def auto_nuevo(request):
    if request.method == "POST":
        form = AutoForm(request.POST, request.FILES)  # Agregamos request.FILES aquí
        if form.is_valid():
            if 'imagen' in request.FILES:  # Verificamos si hay imagen
                auto = form.save()
                auto.imagen = request.FILES['imagen']
                auto.save()
            else:
                auto = form.save()
            return redirect('home')
    else:
        form = AutoForm()
    return render(request, 'blog/auto_form.html', {'form': form})

def reseña_nueva(request):
    if request.method == "POST":
        form = ReseñaForm(request.POST)
        if form.is_valid():
            reseña = form.save()
            return redirect('home')
    else:
        form = ReseñaForm()
    return render(request, 'blog/reseña_form.html', {'form': form})

def categoria_nueva(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/categoria_form.html', {'form': form})

def buscar(request):
    query = request.GET.get('q')
    if query:
        autos = Auto.objects.filter(
            Q(marca__icontains=query) |
            Q(modelo__icontains=query)
        )
    else:
        autos = []
    return render(request, 'blog/buscar.html', {'autos': autos, 'query': query})

# blog/forms.py
from django import forms
from .models import Auto, Reseña, Categoria

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año', 'descripcion']

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['auto', 'titulo', 'contenido']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'autos']
