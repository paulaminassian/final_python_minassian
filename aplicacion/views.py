from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

#__________________________________________Home
def home(request):
    return render(request, "aplicacion/home.html")

#__________________________________________Clientes

class ClientesList(ListView):
    model = Clientes
    
class ClientesCreate(CreateView):
    model = Clientes
    fields = ["razon_social", "contacto"]
    success_url = reverse_lazy('clientes')

class ClientesUpdate(UpdateView):
    model = Clientes
    fields = ["razon_social", "contacto"]
    success_url = reverse_lazy('clientes')   
    
class ClientesDelete(DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes')   

#__________________________________________Maritimas

class MaritimasList(ListView):
    model = Maritimas
    
class MaritimasCreate(CreateView):
    model = Maritimas
    fields = ["maritima", "contacto"]
    success_url = reverse_lazy('maritimas')

class MaritimasUpdate(UpdateView):
    model = Maritimas
    fields = ["maritima", "contacto"]
    success_url = reverse_lazy('maritimas')   
    
class MaritimasDelete(DeleteView):
    model = Maritimas
    success_url = reverse_lazy('maritimas') 

#__________________________________________Rutas

class RutasList(ListView):
    model = Rutas
    
class RutasCreate(CreateView):
    model = Rutas
    fields = ["origen", "destino"]
    success_url = reverse_lazy('rutas')

class RutasUpdate(UpdateView):
    model = Rutas
    fields = ["origen", "destino"]
    success_url = reverse_lazy('rutas')   
    
class RutasDelete(DeleteView):
    model = Rutas
    success_url = reverse_lazy('rutas') 
    
    
#__________________________________________Precios

class PreciosList(ListView):
    model = Precios
    
class PreciosCreate(CreateView):
    model = Precios
    fields = ["ruta", "precio"]
    success_url = reverse_lazy('precios')

class PreciosUpdate(UpdateView):
    model = Precios
    fields = ["ruta", "precio"]
    success_url = reverse_lazy('precios')   
    
class PreciosDelete(DeleteView):
    model = Precios
    success_url = reverse_lazy('precios') 


#__________________________________________Busquedas%Filtros

def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarClientes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clientes_list= Clientes.objects.filter(razon_social__icontains=patron)
        contexto = {"clientes_list": clientes_list}
        return render(request, "aplicacion/clientes_list.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")