from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.producto.models import BaseModel

# Create your models here.
class Perfil(BaseModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    foto = models.ImageField(
        upload_to='usuarios/',
        null=True,
        blank=True
    )

    telefono = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles" # <--- Esto arregla el nombre en el Admin

    def get_foto_url(self):
        """Retorna la foto subida o la de por defecto"""
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        return os.path.join(settings.STATIC_URL, 'img/user.png')
    
    def __str__(self):
        return self.user.username
    

#crear un perfil cada vez que se crea un nuevo usuario
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
