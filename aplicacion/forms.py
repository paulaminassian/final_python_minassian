from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClientesForm(forms.Form):
    razon_social = forms.CharField(max_length=50, required = True)
    contacto = forms.EmailField(required = True)
    
class MaritimasForm(forms.Form):
    maritima = forms.CharField(max_length=50, required = True)
    contacto = forms.EmailField(required = True)
    
class PreciosForm(forms.Form):
    ruta = forms.CharField(max_length=50, required = True)
    precio = forms.IntegerField(required = True)
    
class RutasForm(forms.Form):
    origen = forms.CharField(max_length=50, required = True)
    destino = forms.CharField(max_length=50, required = True)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    
    
    
