from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, PerfilUpdateForm
from .models import Perfil

# Create your views here.

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')

@login_required
def editar_perfil(request):
    # Obtenemos el perfil o lo creamos si no existe (para usuarios viejos)
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Importante: request.FILES para la foto
        p_form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil)

        if u_form.is_valid() and p_form.is_valid():
            # 1. Guardamos el Usuario
            u_form.save()

            # Antes de guardar el perfil, asignamos quién lo edita
            perfil_obj = p_form.save(commit=False)
            perfil_obj.updated_by = request.user # AUDITORÍA
            perfil_obj.save()

             # Importante para campos ManyToMany (si tuvieras alguno)
            p_form.save_m2m() 
            
            messages.success(request, f'¡Tu perfil ha sido actualizado!')
            return redirect('perfil') # Redirige a la vista de ver perfil
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=perfil)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/editar_perfil.html', context)