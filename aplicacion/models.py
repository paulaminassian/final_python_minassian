from django.db import models

# Create your models here.

class Clientes(models.Model):
    razon_social = models.CharField(max_length=50)
    contacto = models.EmailField()
    
    def __str__(self):
        return f'{self.razon_social}'

class Maritimas(models.Model):
    maritima = models.CharField(max_length=50)
    contacto = models.EmailField()
    
    def __str__(self):
        return f'{self.maritima}'
    
class Rutas(models.Model):
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50) 
    
    def __str__(self):
        return f'{self.origen} - {self.destino}'

    
class Precios(models.Model):
    ruta = models.CharField(max_length = 80)
    precio=models.IntegerField()
    
    def __str__(self):
        return f'{self.ruta}'