from django.urls import path
from AppUsuarios.views import *
from AppUsuarios import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('inicio/', iniciosesion, name= 'Inicio'),
    path('registro/', registro, name= 'Registro'),
    path('logout/', LogoutView.as_view(template_name="AppUsuarios/salir.html"), name= 'Salir'),
    path('editar/', editarUsuario, name= "Editar"),
]