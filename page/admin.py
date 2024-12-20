from django.contrib import admin
from .models import Sliders, Categoria, Servicio, Marca, Sucursal, Ejecutivo, \
    Producto, SubCategoria
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

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    
@admin.register(Ejecutivo)
class EjecutivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sucursal', 'estado')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'subcategoria', 'estado')

@admin.register(SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado')