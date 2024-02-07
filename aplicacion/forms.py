from django import forms

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
    

    
    
