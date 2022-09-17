from contextlib import redirect_stderr
from unicodedata import name
from django.shortcuts import render, redirect
from .models import EMPRESA, PRODUCTO
# Create your views here.
def home(request):
   return render(request, "home.html")

def gestion_producto(request):
   productos = PRODUCTO.objects.all()
   return render(request, "gestion_producto.html", {"productos": productos})

def agregar_producto(request):
   producto_id = request.POST['txtCodigo']
   empresa_id = request.POST['txtEmpresa']
   nombre = request.POST['txtProducto']
   
   producto = PRODUCTO.objects.create(
   producto_id = producto_id,
   empresa_id = EMPRESA.objects.get(empresa_id=empresa_id),
   nombre = nombre,
   c_v_u = 0, 
   p_v_u = 0,
   participacion_ventas = 0)
   
   return redirect('http://127.0.0.1:8000/productos/gestion/')
   

def eliminar_producto(request, producto_id):
   producto = PRODUCTO.objects.get(producto_id = producto_id) 
   producto.delete()
   
   return redirect('http://127.0.0.1:8000/productos/gestion/')

def editar_producto(request, producto_id):
   producto = PRODUCTO.objects.get(producto_id = producto_id) 
   return render(request, "costo_variable.html")

   