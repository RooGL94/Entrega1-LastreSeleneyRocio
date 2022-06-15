from django.db import models

# Create your models here.

class cositas(models.Model):
    Nombre= models.CharField(max_length=40)
    Precio= models.IntegerField()
    Detalles= models.CharField(max_length=150)
    Imagen = models.ImageField(upload_to="productos_imagenes", null=True)
    class Meta:
        verbose_name = "cosas"

class ofertas(models.Model):
    descuento= models.IntegerField()
    requisito= models.CharField(max_length=150)
    objetos= models.CharField(max_length=50)
    foto = models.ImageField(upload_to="productos_imagenes", null=True)
    class Meta:
        verbose_name = "oferton"
    
class segunda_mano(models.Model):
    nombre= models.CharField(max_length=40)
    precio= models.IntegerField()
    detalles= models.CharField(max_length=150)
    imagen = models.ImageField(upload_to="productos_imagenes", null=True)
    class Meta:
        verbose_name = "segunda mano"

    
    

