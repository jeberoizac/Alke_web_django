from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
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

    # Campos para control de registros
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def eliminar_logico(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.modelo} - {self.serie} ({self.get_estado_display()})"