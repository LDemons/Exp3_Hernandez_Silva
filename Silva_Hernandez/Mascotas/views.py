from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm,RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def p_inicio(request):
    return render(request, 'p_inicio.html')

def Sobre_Nosotros(request):
    return render(request, 'Sobre_Nosotros.html')


@login_required
def Ventas(request):
    productos = Producto.objects.raw('select * from productos_producto')
    datos = {'productis': productos}
    return render(request, 'Ventas.html', datos)


def Adopcion(request):
    return render(request, 'Adopcion.html')

def Calculadora(request):
    return render(request, 'Calculadora.html')

def registrar(request):
    data = {
        'form' : RegistroUserForm()         
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data = request.POST)  
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],
                  password=formulario.cleaned_data["password1"])
            login(request,user)   
            return redirect('p_inicio')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

@login_required
def crear(request):
    if request.method == "POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()  # similar al insert de sql en función
            return redirect('ventas')
    else:
        productoform = ProductoForm()
    return render(request, 'Crear.html', {'producto_form': productoform})

@login_required
def modificar(request, id):
    productoModificado = Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductoForm(instance=productoModificado)
    }
    if request.method == 'POST':
        formularioo2 = ProductoForm(
            data=request.POST, instance=productoModificado)
        if formularioo2.is_valid:
            formularioo2.save()
            return redirect('Ventas')
    return render(request, 'modificar.html', datos)

@login_required
def eliminar(request, id):
    productoEliminado = Producto.objects.get(idProducto=id)
    productoEliminado.delete()
    return redirect('Ventas')

def mostrar(request):
    productis = Producto.objects.all()
    datos={
        'productis': productis
    }
    return render(request,'mostrar.html',datos)