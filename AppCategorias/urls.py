from django.urls import path
from AppCategorias.views import *
from AppCategorias import views
urlpatterns = [
    path('', inicio, name= "inicio"),
    path('about/', about, name='About' ),
    #URLS DE NOTICIAS
    path('noticias/list', views.noticiasList.as_view(), name= 'Noticias Lista'),
    path('noticias/<int:pk>', views.noticiasDetalle.as_view(), name= 'Noticias Detalles'),
    path('noticias/crear', views.noticiasCreacion.as_view(), name= 'Noticias Crear'),
    path('noticias/editar/<int:pk>', views.noticiasUpdate.as_view(), name= 'Noticias Editar'),
    path('noticias/eliminar/<int:pk>', views.noticiasDelete.as_view(), name= 'Noticias Eliminar'),
    #URLS DE PAPERS
    path('papers/list', views.papersList.as_view(), name= 'Papers Lista'),
    path('papers/<int:pk>', views.papersDetalle.as_view(), name= 'Papers Detalles'),
    path('papers/crear', views.papersCreacion.as_view(), name= 'Papers Crear'),
    path('papers/editar/<int:pk>', views.papersUpdate.as_view(), name= 'Papers Editar'),
    path('papers/eliminar/<int:pk>', views.papersDelete.as_view(), name= 'Papers Eliminar'),
    #path('papers/agregarImagen', subirimagenes, name= 'Subir Imagen'),
    #URLS DE REFLEXIONES
    path('reflexiones/list', views.reflexionesList.as_view(), name= 'ReflexNot Lista'),
    path('reflexiones/<int:pk>', views.reflexionesDetalle.as_view(), name= 'ReflexNot Detalles'),
    path('reflexiones/crear', views.reflexionesCreacion.as_view(), name= 'ReflexNot Crear'),
    path('reflexiones/editar/<int:pk>', views.reflexionesUpdate.as_view(), name= 'ReflexNot Editar'),
    path('reflexiones/eliminar/<int:pk>', views.reflexionesDelete.as_view(), name= 'ReflexNot Eliminar'),
   
    #URL DE REGISTRO  EXITOSO
    path('registroExitoso', registroexitoso, name= 'Registro Exitoso'),

    #URL DE BUSQUEDAS
    path('busquedaNoticia', busquedaNoticia, name= "Busqueda Noticia"),
    path('resultadoNoticia', resultadoNoticia, name= "Resultado Noticia"),
    path('busquedaPapers', busquedaPapers, name= "Busqueda Papers"),
    path('resultadoPapers', resultadoPapers, name= "Resultado Papers"),
    

]