from django.contrib import admin
from .models import Perfil

# Register your models here.
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'updated_at', 'updated_by')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    fieldsets = (
        ('Usuario Asociado', {
            'fields': ('user', 'telefono', 'foto')
        }),
        ('Registro de Actividad', {
            'fields': (('created_by', 'created_at'), ('updated_by', 'updated_at')),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)