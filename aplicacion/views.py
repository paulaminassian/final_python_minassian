from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html")

def clientes(request):
    contexto = {'clientes': Clientes.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto)

def maritimas(request):
    contexto = {'maritimas': Maritimas.objects.all()}
    return render(request, "aplicacion/maritimas.html", contexto)

def rutas(request):
    contexto = {'rutas': Rutas.objects.all()}
    return render(request, "aplicacion/rutas.html", contexto)

def precios(request):
    contexto = {'precios': Precios.objects.all()}
    return render(request, "aplicacion/precios.html", contexto)


def clientesForm(request):
    if request.method == "POST":
        miForm = ClientesForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("razon_social")
            cliente_contacto = miForm.cleaned_data.get("contacto")
            cliente = Clientes(razon_social=cliente_nombre, contacto=cliente_contacto)
            cliente.save()
            return render(request, "aplicacion/home.html")
    else:  
        miForm = ClientesForm()
    
    return render(request, "aplicacion/clientesForm.html", {"form": miForm})

def maritimasForm(request):
    if request.method == "POST":
        miForm = MaritimasForm(request.POST)
        if miForm.is_valid():
            maritima_nombre = miForm.cleaned_data.get("maritima")
            maritima_contacto = miForm.cleaned_data.get("contacto")
            maritimas = Maritimas(maritima=maritima_nombre, contacto=maritima_contacto)
            maritimas.save()
            return redirect("home")
    else:  
        miForm = MaritimasForm()
    
    return render(request, "aplicacion/maritimasForm.html", {"form": miForm})

def rutasForm(request):
    if request.method == "POST":
        miForm = RutasForm(request.POST)
        if miForm.is_valid():
            ruta_origen = miForm.cleaned_data.get("origen")
            ruta_destino = miForm.cleaned_data.get("destino")
            rutas = Rutas(origen=ruta_origen, destino=ruta_destino)
            rutas.save()
            return render(request, "aplicacion/home.html")
    else:  
        miForm = RutasForm()
    
    return render(request, "aplicacion/rutasForm.html", {"form": miForm})


def preciosForm(request):
    if request.method == "POST":
        miForm = PreciosForm(request.POST)
        if miForm.is_valid():
            precio_ruta = miForm.cleaned_data.get("ruta")
            precio_valor = miForm.cleaned_data.get("precio")
            precios = Precios(ruta=precio_ruta, precio=precio_valor)
            precios.save()
            return render(request, "aplicacion/home.html")
    else:  
        miForm = PreciosForm()
    
    return render(request, "aplicacion/preciosForm.html", {"form": miForm})

def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarClientes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clientes = Clientes.objects.filter(razon_social__icontains=patron)
        contexto = {"clientes": clientes}
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")