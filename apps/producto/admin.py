from django.contrib import admin
from .models import Producto

# Register your models here.
admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Esto controla qué columnas ves en la lista principal
    list_display = ('modelo', 'serie', 'estado', 'fecha_ingreso', 'fecha_salida', 'created_at', 'created_by')
    
    # Esto añade una barra de búsqueda por serie o modelo
    search_fields = ('serie', 'modelo')
    
    # Esto añade filtros laterales por estado
    list_filter = ('estado', 'marca')

    # Permite cambiar el estado desde la lista sin entrar al producto
    list_editable = ('estado',)

    # IMPORTANTE: Estos campos no se pueden editar a mano
    readonly_fields = ('created_at', 'updated_at', 'deleted_at', 'created_by', 'updated_by')

    # Organizar el formulario por secciones
    fieldsets = (
        ('Información Técnica', {
            'fields': ('marca', 'modelo', 'serie', 'estado')
        }),
        ('Detalles del Cambio', {
            'classes': ('collapse',), # Esta sección aparecerá cerrada por defecto
            'fields': ('serie_retirada', 'observaciones', 'fecha_ingreso', 'fecha_salida')
        }),
        ('Auditoría (Sistema)', {
            'fields': (('created_by', 'created_at'), ('updated_by', 'updated_at'), 'deleted_at'),
        }),
    )

    # Lógica para guardar quién hizo el cambio automáticamente
    def save_model(self, request, obj, form, change):
        if not obj.pk: # Si el objeto es nuevo
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)