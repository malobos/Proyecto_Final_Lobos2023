from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AppUsuarios.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', iniciosesion, name= "Inicio" ),
    path('AppCategorias/', include('AppCategorias.urls')),
    path('AppUsuarios/', include('AppUsuarios.urls')),

]


urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)