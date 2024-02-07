from django.contrib import admin
from django.contrib import admin
from .models import Clientes, Maritimas, Rutas, Precios
# Register your models here.

admin.site.register(Clientes)
admin.site.register(Maritimas)
admin.site.register(Rutas)
admin.site.register(Precios)