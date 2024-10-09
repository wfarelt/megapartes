from django.shortcuts import render
from .models import Sliders, Categoria, Servicio, Marca, Sucursal

# Create your views here.

def home(request):
    sliders = Sliders.objects.all()
    categories = Categoria.objects.all()
    services = Servicio.objects.all()
    marcas = Marca.objects.all()
    sucursales = Sucursal.objects.all()
    
    return render(request, 'page/home.html', {
        'sliders': sliders, 
        'categories': categories, 
        'services': services, 
        'marcas': marcas, 
        'sucursales': sucursales})

def home2(request):
    return render(request, 'page/base2.html')

def about(request):
    return render(request, 'page/about.html')