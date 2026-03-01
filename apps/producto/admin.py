from django.contrib import admin
from .models import Producto

# Register your models here.
admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Esto controla qué columnas ves en la lista principal
    list_display = ('modelo', 'serie', 'estado', 'fecha_ingreso', 'fecha_salida')
    
    # Esto añade una barra de búsqueda por serie o modelo
    search_fields = ('serie', 'modelo')
    
    # Esto añade filtros laterales por estado
    list_filter = ('estado', 'marca')

    # Permite cambiar el estado desde la lista sin entrar al producto
    list_editable = ('estado',)