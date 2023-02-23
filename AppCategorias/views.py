from collections import UserDict
from django.shortcuts import render
from django.http import HttpResponse
from AppCategorias.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from AppUsuarios.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppCategorias.forms import *

#VISTA DE ACERCA DE MI
def about(request):
    return render(request, "AppCategorias/about.html")

#VISTA DE INICIO
@login_required
def inicio(request):
    usuario= request.user
    return render(request, "AppCategorias/inicio.html", {"mensaje": usuario})

#VISTA DE REGISTRO EXITOSO DE INGRESOS
def registroexitoso(request):
    return render(request, "AppCategorias/registro_exitoso.html" )

#VISTA PARA SUBIR IMAGENES
#def subirimagenes(request):
#    if request.method == "POST":
#        miFormulario=imagenForm(request.POST, request.FILES) 
#        if miFormulario.is_valid():
#            informacion= miFormulario.cleaned_data
#            imagennueva= imagenPaper(vinculado_con=informacion['vinculado_con'], imagen= informacion['imagen'] )
#            imagennueva.save()
#        return render(request, "AppCategorias/registro_exitoso.html")
#    else:
#        
#        miFormulario=imagenForm()
#    
#    return render(request,"AppCategorias/papers/subir_imagen.html", {"miFormulario": miFormulario} )
#VISTA DE BUSQUEDAS

#BUSQUEDA NOTICIAS

def busquedaNoticia(request):
    return render(request, "AppCategorias/noticias/busquedaNoticia.html")

def resultadoNoticia(request):
    if request.GET["tag1"]:
        tag= request.GET["tag1"]
        noticiasRes= noticias.objects.filter(tag1__icontains= tag)
    
        return render(request, "AppCategorias/noticias/resultadoNoticia.html", {"noticiasRes":noticiasRes, "tag1": tag} )
    else:
        respuesta= "No enviaste datos."
    return HttpResponse(respuesta)

#BUSQUEDA PAPERS

def busquedaPapers(request):
    return render(request, "AppCategorias/papers/busquedaPapers.html")

def resultadoPapers(request):
    if request.GET["tag1"]:
        tag= request.GET["tag1"]
        papersRes= papersLibros.objects.filter(tag1__icontains= tag)
    
        return render(request, "AppCategorias/papers/resultadoPapers.html", {"papersRes":papersRes, "tag1": tag} )
    else:
        respuesta= "No enviaste datos."
    return HttpResponse(respuesta)

#     
#CLASES 

#NOTICIAS
class noticiasList(LoginRequiredMixin, ListView):
    model= noticias
    template_name= "AppCategorias/noticias/noticias_list.html"
class noticiasDetalle(LoginRequiredMixin, DetailView):
    model= noticias
    template_name= "AppCategorias/noticias/noticias_detalle.html"
class noticiasCreacion(LoginRequiredMixin, CreateView):
    model= noticias
    success_url= "/AppCategorias/registroExitoso"
    fields= ['titulo', 'medio', 'url', 'fechaDePublicacion','tag1']
    template_name= "AppCategorias/noticias/noticias_form.html"

class noticiasUpdate(LoginRequiredMixin, UpdateView):
    model= noticias
    success_url= "/AppCategorias/noticias/list"
    fields= ['titulo', 'medio', 'url', 'fechaDePublicacion','tag1']
    template_name= "AppCategorias/noticias/noticias_form.html"

class noticiasDelete(DeleteView):
    model= noticias
    success_url= "/AppCategorias/noticias/list"
    template_name= "AppCategorias/noticias/noticias_confirm_delete.html"

#PAPERS Y LIBROS

class papersList(LoginRequiredMixin, ListView):
    model= papersLibros
    template_name= "AppCategorias/papers/papers_list.html"
class papersDetalle(LoginRequiredMixin, DetailView):
    model= papersLibros
    template_name= "AppCategorias/papers/papers_detalle.html"
class papersCreacion(LoginRequiredMixin, CreateView):
    model= papersLibros
    success_url= "/AppCategorias/registroExitoso"
    fields= ['titulo', 'autor1','autor2', 'url', 'editorial', 'imagen','reseña','tag1']
    template_name= "AppCategorias/papers/papers_form.html"

class papersUpdate(LoginRequiredMixin, UpdateView):
    model= papersLibros
    success_url= "/AppCategorias/papers/list"
    fields= ['titulo', 'autor1','autor2', 'url', 'editorial','imagen', 'reseña','tag1']
    template_name= "AppCategorias/papers/papers_form.html"

class papersDelete(DeleteView):
    model= papersLibros
    success_url= "/AppCategorias/papers/list"
    template_name= "AppCategorias/papers/papers_confirm_delete.html"

#REFLEXIONES NOTICIAS

class reflexionesList(LoginRequiredMixin, ListView):
    model= reflexionesNoticias
    template_name= "AppCategorias/reflexiones/reflexnot_list.html"
class reflexionesDetalle(LoginRequiredMixin, DetailView):
    model= reflexionesNoticias
    template_name= "AppCategorias/reflexiones/reflexnot_detalle.html"
class reflexionesCreacion(LoginRequiredMixin, CreateView):
    model= reflexionesNoticias
    success_url= "/AppCategorias/registroExitoso"
    fields= ['relacionado_con_noticia','relacionado_con_publicacionCientifica', 'titulo', 'usuario', 'contenido']
    template_name= "AppCategorias/reflexiones/reflexnot_form.html"

class reflexionesUpdate(LoginRequiredMixin, UpdateView):
    model= reflexionesNoticias
    success_url= "/AppCategorias/reflexiones/list"
    fields= ['relacionado_con_noticia','relacionado_con_publicacionCientifica','titulo', 'usuario', 'contenido']
    template_name= "AppCategorias/reflexiones/reflexnot_form.html"

class reflexionesDelete(DeleteView):
    model= reflexionesNoticias
    success_url= "/AppCategorias/reflexiones/list"
    template_name= "AppCategorias/reflexiones/reflexnot_confirm_delete.html"


