from django.contrib import admin

from .models import Autor, Categoria, Articulo, CategoriaAutor, Comentario

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'titulo', 'categoria_autor',
                    'destacado', 'visible', 'imagen')
    search_fields = ('titulo', 'user__username', 'user__email')
    list_filter = ('creacion', 'actualizacion')
    list_editable = ('categoria_autor', 'destacado', 'visible',)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url',)
        form = super(ArticuloAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['perfil'].initial = request.user.perfil
        return form


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(CategoriaAutor)
class CategoriaAutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'autor')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'articulo', 'comentario', 'visible')
