from django.contrib import admin
from .models import Sliders, Categoria, Servicio
# Register your models here.

@admin.register(Sliders)
class SlidersAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'estado')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')