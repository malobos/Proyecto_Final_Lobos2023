from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from AppUsuarios.forms import *

#vISTAS PARA CREAR USUARIO Y REGISTRARSE

def iniciosesion(request): 
    if request.method == "POST":
        form= AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get("username")
            passw= form.cleaned_data.get("password")

            user= authenticate(username= usuario, password= passw) 
            if user:
                login(request,user)
                return render(request, "AppCategorias/inicio.html", {"mensaje": f"{user}"})
 
            else:
                return render(request,"AppCategorias/inicio.html", {"mensaje":"Datos incorrectos."})
    else:
            form=AuthenticationForm()
    return render(request, "AppUsuarios/inicio_usuario.html", {"formulario": form})

def registro (request):
     if request.method == "POST":
        form= UsuarioRegistro(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render (request, "AppUsuarios/registro_exitoso_usuario.html", {"mensaje": "USUARIO CREADO CORRECTAMENTE :)"})
     else:

        form= UsuarioRegistro()
     return render(request, "AppUsuarios/registro.html", {"formulario": form})

def editarUsuario(request):
    usuario= request.user
    if request.method =="POST":
        form= FormularioEditar(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            usuario.email= info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name= info["first_name"]
            usuario.last_name= info["last_name"]

            usuario.save() 
            return render(request, "AppUsuarios/modificacion_exitosa.html")  
    else: 
        form= FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
        })
    return render (request, "AppCategorias/editarPerfil.html", {"formulario": form, "usuario": usuario})          

