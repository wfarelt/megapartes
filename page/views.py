from django.shortcuts import render
from .models import Sliders, Categoria, Servicio

# Create your views here.

def home(request):
    sliders = Sliders.objects.all()
    categories = Categoria.objects.all()
    services = Servicio.objects.all()
    return render(request, 'page/home.html', {'sliders': sliders, 'categories': categories, 'services':services})