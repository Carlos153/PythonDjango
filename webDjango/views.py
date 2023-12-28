from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg 
from django.contrib.auth import authenticate
from django.shortcuts import redirect

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuarios = authenticate(username=username, password=password)
        if usuarios:
            lg(request,usuarios)
            return redirect('index')
        

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