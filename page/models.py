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

#Sucursal
class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()
    telefono = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='sucursales/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Sucursales"
        
# Ejecutivo de Ventas
class Ejecutivo(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.EmailField()
    imagen = models.ImageField(upload_to='ejecutivos/')
    sucursal = models.ForeignKey(Sucursal, related_name='ejecutivos', on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ejecutivos"
        