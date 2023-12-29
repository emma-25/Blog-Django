from django.urls import path

from .views import LoginView, RegistroView, RegistroOkTemplateView, CustomLogoutView

app_name = 'apps.users'

urlpatterns = [

    path(
        route='login',
        view=LoginView.as_view(),
        name='login'
    ),
    path(
        route='registro',
        view=RegistroView.as_view(),
        name='registro'
    ),
    path(
        route='logout/',
        view=CustomLogoutView.as_view(),
        name='logout'
    ),
    path(
        route='registro_completado/',
        view=RegistroOkTemplateView.as_view(),
        name='registrook'
    ),
]
