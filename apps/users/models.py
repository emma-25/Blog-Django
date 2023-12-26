from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    imagen = models.ImageField(
        upload_to='users/imagenes',
        blank= True,
        null= True
    )
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

