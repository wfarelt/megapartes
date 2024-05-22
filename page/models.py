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