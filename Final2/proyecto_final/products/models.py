from django.db import models

# Create your models here.

class cositas(models.Model):
    Nombre= models.CharField(max_length=40)
    Precio= models.IntegerField()
    Detalles= models.CharField(max_length=150)
    Imagen = models.ImageField(upload_to="productos_imagenes", null=True)
    class Meta:
        verbose_name = "cosas"
