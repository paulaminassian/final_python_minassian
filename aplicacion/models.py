from django.db import models

# Create your models here.

class Clientes(models.Model):
    razon_social = models.CharField(max_length=50)
    contacto = models.EmailField()

class Maritimas(models.Model):
    maritima = models.CharField(max_length=50)
    contacto = models.EmailField()
    
class Rutas(models.Model):
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50) 
    
class Precios(models.Model):
    ruta = models.CharField(max_length = 80)
    precio=models.IntegerField()

