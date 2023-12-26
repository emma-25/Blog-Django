import os
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria, Articulo, Comentario, Contacto
from .forms import CrearComentarioForm, ArticuloForm, ContactoForm 

class ArticuloCreateView(UserPassesTestMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'blog/articulo/crear_articulo.html'
    success_url = reverse_lazy('blog:inicio')
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Administrador', 'Colaborador']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Agregar Articulo'
        return context
    
class ArticuloUpdateView(UserPassesTestMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'blog/articulo/crear_articulo.html'
    slug_field = 'url'
    slug_url_kwarg = 'url'
    success_url = reverse_lazy('blog:inicio')
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Administrador']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos) or self.request.user == self.get_object().user

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Actualizar Articulo'
        return context
    
class ArticuloDeleteView(UserPassesTestMixin, DeleteView):
    model = Articulo
    slug_field = 'url'
    slug_url_kwarg = 'url'
    success_url = reverse_lazy('blog:inicio')
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Administrador']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos) or self.request.user == self.get_object().user

    def form_valid(self, form):
        # Obtener el objeto Articulo
        articulo = self.get_object()

        # Eliminar la imagen adociada
        if articulo.imagen:
            # Obtener la ruta completa del archivo de imagen
            image_path = articulo.imagen.path

            # Verificar si el archivo existe y eliminarlo
            if os.path.exists(image_path):
                os.remove(image_path)

        return super().form_valid(form)

class InicioListView(ListView):
    model = Articulo
    template_name = 'blog/index.html'
    context_object_name = 'articulos'
    ordering = ('-creacion',) 
    queryset = Articulo.objects.filter(visible=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos'] = Articulo.objects.all()
        context['articulos_destacados'] = Articulo.objects.filter(destacado=True, visible=True)
        return context
    
class NosotrosTemplateView(TemplateView):
    template_name = 'blog/nosotros.html'

class ContactoFormView(FormView):
    form_class = ContactoForm
    template_name = 'blog/contacto.html'
    success_url = reverse_lazy('blog:contactook')

class ContactoTemplateView(TemplateView):
    template_name = 'blog/contactook.html'
    
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'blog/detalle.html'
    context_object_name = 'articulo'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos'] = Articulo.objects.filter(visible=True)
        context['categorias'] = Categoria.objects.all()
        context['comentarios'] = Comentario.objects.filter(
            visible=True, articulo=self.get_object()).all()
        context['cantidad_comentarios'] = Comentario.objects.filter(
            visible=True, articulo=self.get_object()).all().count()
        return context
    
class ComentarioView(UserPassesTestMixin, View):
    template_name = 'blog/detalle.html'
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Colaborador', 'Administrador', 'Registrado']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos)

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=405)

    def post(self, request, *args, **kwargs):
        url = request.POST.get('url')
        articulo = {
            'user': request.user.id,
            'perfil': request.user.perfil.id,
            'comentario': request.POST.get('comentario'),
            'articulo': request.POST.get('articulo')
        }
        form = CrearComentarioForm(articulo)
        if form.is_valid():
            form.save()
            return redirect('blog:detalle', url=url)
        else:
            return HttpResponse(status=500)
    
class CategoriaListView(ListView):
    model = Articulo
    template_name = 'blog/index.html'
    context_object_name = 'articulos'
    paginate_by = 2
    ordering = ('-creacion',)

    def get_queryset(self):
        articulo = None
        if self.kwargs['categoria_id']:
            categoria_id = self.kwargs['categoria_id']
            categoria = Categoria.objects.filter(id=categoria_id)[:1]
            articulo = Articulo.objects.filter(visible=True, categoria_autor__categoria=categoria)
        return articulo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['articulos_destacados'] = Articulo.objects.filter(
            destacado=True, visible=True)
        return context
    
class UserListView(ListView):
    model = Articulo
    template_name = 'blog/index.html'
    context_object_name = 'articulos'
    paginate_by = 2
    ordering = ('-creacion',)

    def get_queryset(self):
        articulo = None
        if self.kwargs['nombre']:
            user_nombre = self.kwargs['nombre']
            user = User.objects.filter(username=user_nombre)[:1]
            articulo = Articulo.objects.filter(visible=True, user=user)
        return articulo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['articulos_destacados'] = Articulo.objects.filter(
            destacado=True, visible=True)
        return context


