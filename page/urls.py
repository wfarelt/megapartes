from django.urls import path
from .views import home, about, catalog

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('catalog', catalog, name='catalog')
]
