from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .forms import ProductoForm

from .models import Producto

# Create your views here.
################  Crud basico de Producto  ################
def lista_producto(request):
     pos = Producto.objects.filter(deleted_at__isnull=True).order_by('-fecha_ingreso')     
       # OJO: Verifica que el nombre del template sea exacto a tu carpeta
     return render(request, 'producto/lista_producto.html', {'productos': pos})

#agregar producto con formulario
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():

            producto = form.save(commit=False) # Creamos el objeto pero no lo guardamos aún
            producto.created_by = request.user # Asignamos el usuario que creó el producto
            producto.save() # Ahora sí guardamos el producto en la base de datos
            messages.success(request, f"El equipo con serie {producto.serie} fue agregado correctamente.")
            return redirect('lista_producto') # Nos manda de vuelta a la lista
        else:
            # Esto imprimirá en tu terminal por qué no guardó (ej: serie duplicada)
            print("Errores del formulario:", form.errors)
    else:
        form = ProductoForm()
    
    return render(request, 'producto/agregar_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(
    Producto,
    pk=producto_id,
    deleted_at__isnull=True
    )
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.updated_by = request.user
            producto.save()
            messages.info(request, f"El equipo con serie {producto.serie} fue editado correctamente.")
            return redirect('lista_producto')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'producto/editar_producto.html', {'form': form, 'producto': producto})


def eliminar_producto(request, producto_id):
    # 1. Buscamos el producto por su ID (pk)
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == 'POST':
        # 2. Si se confirma el envío del formulario, eliminamos
        #producto.delete()
        producto.eliminar_logico()
        # Aquí el mensaje de éxito del borrado, puedes personalizarlo como quieras
        messages.info(request, f"El equipo con serie {producto.serie} fue eliminado correctamente.")
        return redirect('lista_producto')
    
    # 3. Si no es POST, simplemente mostramos la página de confirmación
    return render(request, 'producto/confirmar_eliminar.html', {'producto': producto})