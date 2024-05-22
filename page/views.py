from django.shortcuts import render
from .models import Sliders, Categoria

# Create your views here.

def home(request):
    sliders = Sliders.objects.all()
    categories = Categoria.objects.all()
    return render(request, 'page/home.html', {'sliders': sliders, 'categories': categories})