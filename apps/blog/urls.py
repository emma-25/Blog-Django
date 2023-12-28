from django.urls import path
from .views import InicioListView, NosotrosTemplateView, ContactoFormView, ContactoTemplateView, ArticuloDetailView, ArticuloCreateView, ArticuloUpdateView, ArticuloDeleteView, ComentarioCreateView, ComentarioDeleteView, CategoriaListView, UserListView, OrdenarZAListView, OrdenarAZListView, OrdenarMasAntiguoListView, OrdenarMasNuevoListView

app_name = 'apps.blog'

urlpatterns = [
    path(
        route='',
        view=InicioListView.as_view(),
        name='inicio'
    ),
    path(
        route='nosotros/',
        view=NosotrosTemplateView.as_view(),
        name='nosotros'
    ),
    path(
        route='contacto/',
        view=ContactoFormView.as_view(),
        name='contacto'
    ),
    path(
        route='contactook/',
        view=ContactoTemplateView.as_view(),
        name='contactook'
    ),
    path(
        route='articulo/<slug:url>/',
        view=ArticuloDetailView.as_view(),
        name='detalle'
    ),
    path(
        route='carga_articulo/',
        view=ArticuloCreateView.as_view(),
        name='carga_articulo'
    ),
    path(
        route='actualizar_articulo/<slug:url>/',
        view=ArticuloUpdateView.as_view(),
        name='actualizar_articulo'
    ),
    path(
        route='eliminar_articulo/<slug:url>/',
        view=ArticuloDeleteView.as_view(),
        name='eliminar_articulo'
    ),
    path(
        route='comentario/',
        view=ComentarioCreateView.as_view(),
        name='comentario'
    ),
    path(
        route='eliminar_comentario/<int:pk>/',
        view=ComentarioDeleteView.as_view(),
        name='eliminar_comentario'
    ),
    path(
        route='categoria/<int:categoria_id>/',
        view=CategoriaListView.as_view(),
        name='categoria'
    ),
    path(
        route='user/<str:nombre>/',
        view=UserListView.as_view(),
        name='user'
    ),
    path(
        route='post_orden_mas_nuevos/',
        view=OrdenarMasNuevoListView.as_view(),
        name='ordenar_mas_nuevo'
    ),
    path(
        route='post_orden_mas_antiguos/',
        view=OrdenarMasAntiguoListView.as_view(),
        name='ordenar_mas_antiguo'
    ),   
    path(
        route='post_orden_A_Z/',
        view=OrdenarAZListView.as_view(),
        name='ordenar_A_Z'
    ),   
    path(
        route='post_orden_Z_A/',
        view=OrdenarZAListView.as_view(),
        name='ordenar_Z_A'
    ),
]
