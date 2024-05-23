from django.db import models

# Create your models here.

class Sliders(models.Model):
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='sliders/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion[:50]
    
    class Meta:
        verbose_name_plural = "Sliders"


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorias"

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Servicios"

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='marcas/')
    industria = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Marcas"