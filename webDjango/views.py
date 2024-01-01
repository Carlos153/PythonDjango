from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg 
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import Registro


def login(request):
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
    form = Registro()
    
    return render(request, 'user/registro.html',{
        'form':form

    })

