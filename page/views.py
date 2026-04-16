from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from .models import Sliders, Categoria, Servicio, Marca, Sucursal, \
      Ejecutivo, SubCategoria, Producto
from .forms import EjecutivoForm, MarcaForm, SucursalForm

# Create your views here.

def home(request):
    sliders = Sliders.objects.filter(estado=True)
    categories = Categoria.objects.all()
    services = Servicio.objects.all()
    marcas = Marca.objects.all()
    #Filtrar las ultimas 4 sucursales
    sucursales = Sucursal.objects.filter(estado=True).order_by('id')[:4]
    
    return render(request, 'page/home.html', {
        'sliders': sliders, 
        'categories': categories, 
        'services': services, 
        'marcas': marcas, 
        'sucursales': sucursales,
        })

def about(request):
    ejecutivos = Ejecutivo.objects.filter(estado=True)
    return render(request, 'page/about.html', {'ejecutivos': ejecutivos})


@login_required(login_url='/?login=required')
def catalog(request, id_subcategoria=None):
    if id_subcategoria:
        productos = Producto.objects.filter(subcategoria=id_subcategoria)
    categorias = Categoria.objects.all()
    subcategorias = SubCategoria.objects.all()
    return render(request, 'page/catalog.html', {'categorias': categorias, 'subcategorias': subcategorias})


def _is_staff_user(user):
    return user.is_staff


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method != 'POST':
        return redirect('home')

    default_next_url = reverse('sucursal_panel')
    next_url = request.POST.get('next', '').strip() or default_next_url
    if next_url == '/':
        next_url = default_next_url

    if not url_has_allowed_host_and_scheme(next_url, {request.get_host()}, request.is_secure()):
        next_url = default_next_url

    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(next_url)

    return redirect(f"{reverse('home')}?login=error&next={next_url}")


@login_required
@user_passes_test(_is_staff_user)
def sucursal_panel(request):
    sucursales = Sucursal.objects.order_by('nombre')
    return render(request, 'sucursal/panel.html', {'sucursales': sucursales})


@login_required
@user_passes_test(_is_staff_user)
def sucursal_create(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sucursal creada correctamente.')
            return redirect('sucursal_panel')
    else:
        form = SucursalForm()

    return render(request, 'sucursal/form.html', {
        'form': form,
        'title': 'Nueva sucursal',
        'button_label': 'Crear sucursal',
    })


@login_required
@user_passes_test(_is_staff_user)
def sucursal_update(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)

    if request.method == 'POST':
        form = SucursalForm(request.POST, request.FILES, instance=sucursal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sucursal actualizada correctamente.')
            return redirect('sucursal_panel')
    else:
        form = SucursalForm(instance=sucursal)

    return render(request, 'sucursal/form.html', {
        'form': form,
        'title': f'Editar sucursal: {sucursal.nombre}',
        'button_label': 'Guardar cambios',
    })


@login_required
@user_passes_test(_is_staff_user)
def sucursal_delete(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)

    if request.method == 'POST':
        sucursal.delete()
        messages.success(request, 'Sucursal eliminada correctamente.')
        return redirect('sucursal_panel')

    return render(request, 'sucursal/confirm_delete.html', {'sucursal': sucursal})


@login_required
@user_passes_test(_is_staff_user)
def marca_panel(request):
    marcas = Marca.objects.order_by('nombre')
    return render(request, 'marca/panel.html', {'marcas': marcas})


@login_required
@user_passes_test(_is_staff_user)
def marca_create(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca creada correctamente.')
            return redirect('marca_panel')
    else:
        form = MarcaForm()

    return render(request, 'marca/form.html', {
        'form': form,
        'title': 'Nueva marca',
        'button_label': 'Crear marca',
    })


@login_required
@user_passes_test(_is_staff_user)
def marca_update(request, pk):
    marca = get_object_or_404(Marca, pk=pk)

    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca actualizada correctamente.')
            return redirect('marca_panel')
    else:
        form = MarcaForm(instance=marca)

    return render(request, 'marca/form.html', {
        'form': form,
        'title': f'Editar marca: {marca.nombre}',
        'button_label': 'Guardar cambios',
    })


@login_required
@user_passes_test(_is_staff_user)
def marca_delete(request, pk):
    marca = get_object_or_404(Marca, pk=pk)

    if request.method == 'POST':
        marca.delete()
        messages.success(request, 'Marca eliminada correctamente.')
        return redirect('marca_panel')

    return render(request, 'marca/confirm_delete.html', {'marca': marca})


@login_required
@user_passes_test(_is_staff_user)
def ejecutivo_panel(request):
    ejecutivos = Ejecutivo.objects.select_related('sucursal').order_by('nombre')
    return render(request, 'ejecutivo/panel.html', {'ejecutivos': ejecutivos})


@login_required
@user_passes_test(_is_staff_user)
def ejecutivo_create(request):
    if request.method == 'POST':
        form = EjecutivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ejecutivo creado correctamente.')
            return redirect('ejecutivo_panel')
    else:
        form = EjecutivoForm()

    return render(request, 'ejecutivo/form.html', {
        'form': form,
        'title': 'Nuevo ejecutivo',
        'button_label': 'Crear ejecutivo',
    })


@login_required
@user_passes_test(_is_staff_user)
def ejecutivo_update(request, pk):
    ejecutivo = get_object_or_404(Ejecutivo, pk=pk)

    if request.method == 'POST':
        form = EjecutivoForm(request.POST, request.FILES, instance=ejecutivo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ejecutivo actualizado correctamente.')
            return redirect('ejecutivo_panel')
    else:
        form = EjecutivoForm(instance=ejecutivo)

    return render(request, 'ejecutivo/form.html', {
        'form': form,
        'title': f'Editar ejecutivo: {ejecutivo.nombre}',
        'button_label': 'Guardar cambios',
    })


@login_required
@user_passes_test(_is_staff_user)
def ejecutivo_delete(request, pk):
    ejecutivo = get_object_or_404(Ejecutivo, pk=pk)

    if request.method == 'POST':
        ejecutivo.delete()
        messages.success(request, 'Ejecutivo eliminado correctamente.')
        return redirect('ejecutivo_panel')

    return render(request, 'ejecutivo/confirm_delete.html', {'ejecutivo': ejecutivo})