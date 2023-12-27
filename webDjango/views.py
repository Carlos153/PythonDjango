from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request,'user/login.html',{})
def saludo(request):
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