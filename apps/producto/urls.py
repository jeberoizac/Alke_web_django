from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_producto, name='lista_producto'),
    path('nuevo_pos/', views.agregar_producto, name='agregar_producto'), # Nueva ruta
    path('editar_pos/<int:producto_id>/', views.editar_producto, name='editar_producto'), # Ruta para editar
    path('eliminar_pos/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'), # Ruta para eliminar
]