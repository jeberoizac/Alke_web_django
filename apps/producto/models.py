from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Importamos el modelo de usuario para las relaciones de auditoría
User = get_user_model()

# Create your models here.

#1° Modelo de clase Base
class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    #Metodo para auditar cambios
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_records"
    )

    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_records"
    )

    #Metodo para eliminar logico
    def eliminar_logico(self):
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True

#2° Modelo de clase Producto que hereda de BaseModel
class Producto(BaseModel):
    ESTADO_CHOICES = [
        ('nuevo', 'Disponible (Nuevo) ✨'),
        ('instalado', 'Instalado en Cliente 🏠'),
        ('falla', 'Retirado por Falla ⚠️'),
        ('bodega', 'En Bodega (Para Revisión) 📦'),
        ('cambiado', 'Equipo Sustituido/Cambiado 🔄'),
    ]

    #nombre = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)  # ID autoincremental
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serie = models.CharField(max_length=100, unique=True) # La serie es única
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='nuevo')
    
    # --- Campos para profesionalizar el "Cambio" ---
    serie_retirada = models.CharField(max_length=100, null=True, blank=True, help_text="Si es un cambio, ¿qué serie falló?")
    observaciones = models.TextField(null=True, blank=True)
    
    # --- Trazabilidad ---
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    fecha_salida = models.DateTimeField(null=True, blank=True)

  
    def __str__(self):
        return f"{self.modelo} - {self.serie} ({self.get_estado_display()})"