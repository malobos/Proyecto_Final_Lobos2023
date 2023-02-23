from django.db import models
from django.contrib.auth.models import User

class noticias(models.Model):
    titulo= models.CharField(max_length=200)#para poner el titulo de la noticia
    medio= models.CharField(max_length=40)#para poner el medio (periodico o revista) donde se encuentra la noticia
    url= models.URLField(max_length=200, blank=True, null= True) #para poner la url en el caso que sea digital
    fechaDePublicacion= models.DateField(blank=True ,null= True) #para poner la fecha en que fue publicada la noticia
    fechaDeSubida= models.DateTimeField(auto_now_add=True)
    tag1= models.CharField(max_length=40, blank=True, null= True)
    

    def __str__(self):
            return f"TITULO: {self.titulo}"

class papersLibros(models.Model):
    titulo= models.CharField(max_length=100) #titulo de la publicacion
    autor1= models.CharField(max_length=40) #solo un autor
    autor2= models.CharField(max_length=40, blank= True, null=True) #poner si tiene otro autor (luego podemos agregar mas)
    url= models.URLField(max_length=200, blank=True ,null= True) #para poner la url
    editorial= models.CharField(max_length=100)
    reseña= models.TextField(max_length=2000)
    fechaDeSubida= models.DateTimeField(auto_now_add=True)
    tag1= models.CharField(max_length=40, blank=True, null= True)
    imagen= models.ImageField(upload_to="papers", null=True, blank= True)

    def __str__(self):
            return f"TITULO: {self.titulo}"    
class reflexionesNoticias(models.Model):
    relacionado_con_noticia= models.ForeignKey (noticias, on_delete=models.CASCADE,blank=True, null= True) 
    relacionado_con_publicacionCientifica= models.ForeignKey (papersLibros, on_delete=models.CASCADE, blank=True, null= True) 
    usuario= models.ForeignKey (User, on_delete=models.CASCADE, null=True) 
    titulo= models.CharField(max_length=40)
    contenido= models.TextField(max_length=2000)
    fechaDeSubida= models.DateTimeField(auto_now_add=True)




