from django.urls import path
from .views import (
    about,
    catalog,
    ejecutivo_create,
    ejecutivo_delete,
    ejecutivo_panel,
    ejecutivo_update,
    home,
    login_view,
    logout_view,
    marca_create,
    marca_delete,
    marca_panel,
    marca_update,
    sucursal_create,
    sucursal_delete,
    sucursal_panel,
    sucursal_update,
)

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('catalog/<int:id_subcategoria>', catalog, name='catalog'),

    path('config/ejecutivos/', ejecutivo_panel, name='ejecutivo_panel'),
    path('config/ejecutivos/nuevo/', ejecutivo_create, name='ejecutivo_create'),
    path('config/ejecutivos/<int:pk>/editar/', ejecutivo_update, name='ejecutivo_update'),
    path('config/ejecutivos/<int:pk>/eliminar/', ejecutivo_delete, name='ejecutivo_delete'),
    
    path('config/marcas/', marca_panel, name='marca_panel'),
    path('config/marcas/nueva/', marca_create, name='marca_create'),
    path('config/marcas/<int:pk>/editar/', marca_update, name='marca_update'),
    path('config/marcas/<int:pk>/eliminar/', marca_delete, name='marca_delete'),
    
    path('config/sucursales/', sucursal_panel, name='sucursal_panel'),
    path('config/sucursales/nueva/', sucursal_create, name='sucursal_create'),
    path('config/sucursales/<int:pk>/editar/', sucursal_update, name='sucursal_update'),
    path('config/sucursales/<int:pk>/eliminar/', sucursal_delete, name='sucursal_delete'),
]
