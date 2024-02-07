from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', home, name = "home"),
    path('clientes/', clientes, name = "clientes"),
    path('maritimas/', maritimas, name = "maritimas"),
    path('rutas/', rutas, name = "rutas"),
    path('precios/', precios, name = "precios"),
    
    path('clientes_form/', clientesForm, name = "clientes_form"),
    path('maritimas_form/', maritimasForm, name = "maritimas_form"),
    path('rutas_form/', rutasForm, name = "rutas_form"),
    path('precios_form/', preciosForm, name = "precios_form"),
    
    path('buscar/', buscar, name = "buscar"),
    path('buscar_clientes/', buscarClientes, name = "buscar_clientes"),

]
