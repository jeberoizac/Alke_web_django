from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# def index(request):
#     return HttpResponse("<h1>Bienvenidos a Alke Solutions</h1>")

#pagina de inicio
@login_required
def index(request):
    return render(request, 'home/home.html')

#pagina de contacto
@login_required
def contacto(request):
    return render(request, 'home/contacto.html')
