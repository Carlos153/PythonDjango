from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg 
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import Registro
from django.contrib.auth.models import User



def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuarios = authenticate(username=username, password=password)
        if usuarios:
            lg(request,usuarios)
            messages.success(request, f'Bienvendo {usuarios.username}')
            return redirect('index')
        else:
            messages.error(request,'Datos erroneos')
        

    return render(request,'user/login.html',{})


def index(request):
    return render(request,'index.html',{
        'mensaje': 'Tienda',
        'titulo' : 'Inicio',
        'productos':[
            {'titulo':'Sudadera','precio': 15,'stock':False},
            {'titulo':'Camiseta','precio': 18,'stock':True},
            {'titulo':'Chaqueta','precio': 15,'stock':False},
            {'titulo':'Gorra','precio': 55,'stock':True}
        ] 
     
    })


def salir(request):
    logout(request)
    messages.success(request,'Sesion cerrada')
    return redirect(login)

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = Registro(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        usuario = form.save()
        if usuario:
            lg(request, usuario)
            messages.success(request, 'Bienvenido')
            return redirect('index')

    return render(request, 'user/registro.html', {'form': form})
    

