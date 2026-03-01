from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("<h1>Bienvenidos a Alke Solutions</h1>")

#pagina de inicio
def index(request):
    return render(request, 'home/home.html')

#pagina de contacto
def contacto(request):
    return render(request, 'home/contacto.html')
