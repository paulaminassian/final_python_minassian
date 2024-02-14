from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #____________________________________Home
    path('', home, name = "home"),
    
    #____________________________________Clientes
    path('clientes/', ClientesList.as_view(), name="clientes"),
    path('clientes_create/', ClientesCreate.as_view(), name="cliente_create"),
    path('clientes_update/<int:pk>/', ClientesUpdate.as_view(), name="cliente_update"),
    path('clientes_delete/<int:pk>/', ClientesDelete.as_view(), name="cliente_delete"),
    
    #____________________________________Maritimas
    path('maritimas/', MaritimasList.as_view(), name="maritimas"),
    path('maritimas_create/', MaritimasCreate.as_view(), name="maritima_create"),
    path('maritimas_update/<int:pk>/', MaritimasUpdate.as_view(), name="maritima_update"),
    path('maritimas_delete/<int:pk>/', MaritimasDelete.as_view(), name="maritima_delete"),
    
    #____________________________________Rutas
    path('rutas/', RutasList.as_view(), name="rutas"),
    path('rutas_create/', RutasCreate.as_view(), name="ruta_create"),
    path('rutas_update/<int:pk>/', RutasUpdate.as_view(), name="ruta_update"),
    path('rutas_delete/<int:pk>/', RutasDelete.as_view(), name="ruta_delete"),
    
    #____________________________________Precios
    path('precios/', PreciosList.as_view(), name="precios"),
    path('precios_create/', PreciosCreate.as_view(), name="precio_create"),
    path('precios_update/<int:pk>/', PreciosUpdate.as_view(), name="precio_update"),
    path('precios_delete/<int:pk>/', PreciosDelete.as_view(), name="precio_delete"),
    

    #____________________________________Busquedas&Filtros
    path('buscar/', buscar, name = "buscar"),
    path('buscar_clientes/', buscarClientes, name = "buscar_clientes"),
    
    #____________________________________login,logout, registro
    path('login/', login_request, name = "login"),
    path('registro/', register, name = "registro"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name = "logout"),
    
]
