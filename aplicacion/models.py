from django.db import models

# Create your models here.

class Clientes(models.Model):
    razon_social = models.CharField(max_length=50)
    contacto = models.EmailField()
    
    def __str__(self):
        return f'Cliente: {self.razon_social} - Contacto: {self.contacto}'
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Maritimas(models.Model):
    maritima = models.CharField(max_length=50)
    contacto = models.EmailField()
    
    def __str__(self):
        return f' Maritima: {self.maritima} - Contacto: {self.contacto}'
    
    class Meta:
        verbose_name = "Maritima"
        verbose_name_plural = "Maritimas"
    
class Rutas(models.Model):
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50) 
    
    def __str__(self):
        return f' Origen: {self.origen} - Destino: {self.destino}'
    
    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"

    
class Precios(models.Model):
    ruta = models.CharField(max_length = 80)
    precio=models.IntegerField()
    
    def __str__(self):
        return f'Ruta:{self.ruta} - Precio: {self.precio}'
    
    class Meta:
        verbose_name = "Precio"
        verbose_name_plural = "Precios"