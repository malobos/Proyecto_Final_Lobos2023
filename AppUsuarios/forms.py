from django import forms
from django.contrib.auth.forms import UserCreationForm       
from django.contrib.auth.models import User
class UsuarioRegistro(UserCreationForm):
    email= forms.EmailField()
    nombre=forms.CharField()
    apellido= forms.CharField() 
    password1= forms.CharField(label= "Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label= "Repetir la contraseña", widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ["username", "email", "password1", "password2"]     

class FormularioEditar(UserCreationForm):
    
    email= forms.EmailField()
    first_name=forms.CharField(label= "Nombre")
    last_name= forms.CharField(label= "Apellido")
    password1= forms.CharField(label= "Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label= "Repetir la contraseña", widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ["email", "password1", "password2"]     
