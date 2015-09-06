from django.shortcuts import render, get_object_or_404
from .models import Entrada
from django.utils import timezone
from forms import FormEntrada
from . import models
from django.shortcuts import redirect

def lista_entradas(request):
    entradas = Entrada.objects.filter(fecha_publi__lte=timezone.now()).order_by('fecha_publi')
    return render(request, 'blog/lista_entradas.html', {'entradas':entradas})
    
def detalle_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'blog/detalle_entrada.html', {'entrada': entrada})
    
def nueva_entrada(request):
    if request.method == "POST":
        form = FormEntrada(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.autor = request.user
            entrada.fecha_publi = timezone.now()
            entrada.save()
            return redirect('blog.views.detalle_entrada', pk=entrada.pk)
    else:
        form = FormEntrada()
    return render(request, 'blog/editar_entrada.html', {'form': form})
    
def editar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == "POST":
        form = FormEntrada(request.POST, instance=entrada)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.autor = request.user
            entrada.fecha_publi = timezone.now()
            entrada.save()
            return redirect('blog.views.detalle_entrada', pk=entrada.pk)
    else:
        form = FormEntrada(instance=entrada)
    return render(request, 'blog/editar_entrada.html', {'form': form})