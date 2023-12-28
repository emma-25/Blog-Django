from django.db import models

from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()
from ckeditor.fields import RichTextField
from apps.users.models import Perfil

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('nombre',)
   
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('nombre',)
    
    def __str__(self):
        return self.nombre

class CategoriaAutor(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return f'{self.autor} - {self.categoria}'
    
class Articulo(models.Model):
    categoria_autor = models.ForeignKey(CategoriaAutor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=255, unique=True)
    url = models.SlugField(max_length=255, unique=True)
    resumen = RichTextField()
    contenido = RichTextField()
    vistas = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    imagen = models.ImageField(upload_to='articulo/imagenes/')

    class Meta:
        ordering = ('creacion',)

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Articulo, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.categoria_autor} - {self.user.username}'
    

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=5000)
    visible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    
