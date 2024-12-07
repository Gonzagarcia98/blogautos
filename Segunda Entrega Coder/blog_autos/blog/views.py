from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto, Categoria
from .forms import AutoForm, ReseñaForm, CategoriaForm
from django.db.models import Q

def home(request):
    autos = Auto.objects.all()
    return render(request, 'blog/home.html', {'autos': autos})

def auto_nuevo(request):
    if request.method == "POST":
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            if 'imagen' in request.FILES:  
                auto = form.save()
                auto.imagen = request.FILES['imagen']
                auto.save()
            else:
                auto = form.save()
            return redirect('home')
    else:
        form = AutoForm()
    return render(request, 'blog/auto_form.html', {'form': form})

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
    categorias_existentes = Categoria.objects.all()
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/categoria_form.html', {
        'form': form,
        'categorias_existentes': categorias_existentes
    })

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

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/lista_categorias.html', {'categorias': categorias})
