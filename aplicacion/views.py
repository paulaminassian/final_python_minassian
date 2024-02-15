from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

#__________________________________________Home
def home(request):
    return render(request, "aplicacion/home.html")

#__________________________________________Clientes

class ClientesList(LoginRequiredMixin, ListView):
    model = Clientes

    
class ClientesCreate(LoginRequiredMixin, CreateView):
    model = Clientes
    fields = ["razon_social", "contacto"]
    success_url = reverse_lazy('clientes')

class ClientesUpdate(LoginRequiredMixin, UpdateView):
    model = Clientes
    fields = ["razon_social", "contacto"]
    success_url = reverse_lazy('clientes')   
    
class ClientesDelete(LoginRequiredMixin, DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes')   

#__________________________________________Maritimas

class MaritimasList(LoginRequiredMixin, ListView):
    model = Maritimas
    
class MaritimasCreate(LoginRequiredMixin, CreateView):
    model = Maritimas
    fields = ["maritima", "contacto"]
    success_url = reverse_lazy('maritimas')

class MaritimasUpdate(LoginRequiredMixin, UpdateView):
    model = Maritimas
    fields = ["maritima", "contacto"]
    success_url = reverse_lazy('maritimas')   
    
class MaritimasDelete(LoginRequiredMixin, DeleteView):
    model = Maritimas
    success_url = reverse_lazy('maritimas') 

#__________________________________________Rutas

class RutasList(LoginRequiredMixin, ListView):
    model = Rutas
    
class RutasCreate(LoginRequiredMixin, CreateView):
    model = Rutas
    fields = ["origen", "destino"]
    success_url = reverse_lazy('rutas')

class RutasUpdate(LoginRequiredMixin, UpdateView):
    model = Rutas
    fields = ["origen", "destino"]
    success_url = reverse_lazy('rutas')   
    
class RutasDelete(LoginRequiredMixin, DeleteView):
    model = Rutas
    success_url = reverse_lazy('rutas') 
    
    
#__________________________________________Precios

class PreciosList(LoginRequiredMixin, ListView):
    model = Precios
    
class PreciosCreate(LoginRequiredMixin, CreateView):
    model = Precios
    fields = ["ruta", "precio"]
    success_url = reverse_lazy('precios')

class PreciosUpdate(LoginRequiredMixin, UpdateView):
    model = Precios
    fields = ["ruta", "precio"]
    success_url = reverse_lazy('precios')   
    
class PreciosDelete(LoginRequiredMixin, DeleteView):
    model = Precios
    success_url = reverse_lazy('precios') 


#__________________________________________Busquedas%Filtros
@login_required
def buscar(request):
    return render(request, "aplicacion/buscar.html")
@login_required
def buscarClientes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clientes_list= Clientes.objects.filter(razon_social__icontains=patron)
        contexto = {"clientes_list": clientes_list}
        return render(request, "aplicacion/clientes_list.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")


#__________________________________________Login, Logout, Registro


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            password = miForm.cleaned_data.get("password")
            user = authenticate(username = usuario, password = password)
            if user is not None:
                login(request, user)
                
                
                #___________Avatar
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                    
                    
                return redirect(reverse_lazy('home'))   
            else:
                return redirect(reverse_lazy('login'))
                    
    else:
        miForm = AuthenticationForm()
        
    return(render(request, "aplicacion/login.html", {"form": miForm}))


def register(request):
        if request.method == "POST":
            miForm = RegistroForm(request.POST)
            if miForm.is_valid():
                usuario = miForm.cleaned_data.get("username")
                miForm.save()      
                return redirect(reverse_lazy('home'))
            
                            
        else:
            miForm = RegistroForm()
            
        return(render(request, "aplicacion/registro.html", {"form": miForm}))
    
    



#_____________________________________________Editar perfil de usuario
@login_required
def editarPerfil(request):
    usuario = request.user
    
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:
        form=UserEditForm(instance=usuario)
        
    return render(request, "aplicacion/editarPerfil.html", {"form": form})



#_______________________________________________

@login_required
def agregarAvatar(request):
    
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)
            
            #para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #_____________________
            avatar = Avatar(user=usuario,imagen=form.cleaned_data['imagen'])
            avatar.save()
            
            
            #_____________________hagu una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/home.html")
        
    else:
        form = AvatarForm()
        
    return render(request, "aplicacion/agregarAvatar.html", {"form": form})
    

    
        
        
        
    
    
        