from distutils import errors
from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Empresa, FormConcepto, Producto,FormProducto,Concepto
from django.core.exceptions import ValidationError
from django.contrib import messages
# Create your views here.
def home(request):
   return render(request, "home.html")

def registro(request):
   return render(request, "registro.html")

def costos(request, empresa_id=1):
   if request.method == 'POST':
    
      form = FormProducto(request.POST)

      if form.is_valid():

         producto = Producto.objects.create(

         empresa_id = Empresa.objects.get(id=empresa_id),
         nombre = form.cleaned_data['nombre'],
         c_v_u = form.cleaned_data['c_v_u'], 
         p_v_u = form.cleaned_data['p_v_u'],
         participacion_ventas = form.cleaned_data['participacion_ventas'])

         
         producto.save()
         messages.success(request, 'producto añadido correctamente')

      else:
         print(form.errors)
         if(not form.errors):
            messages.success(request, 'Producto ya registrado')
         
         # raise ValidationError(('Producto ya se encuentra registrado'))


   productos = Producto.objects.filter(empresa_id=empresa_id)

   form = FormProducto()

   return render(request, "costos.html", {"productos": productos,'form':form})      


def gestion_producto(request,empresa_id=1): #donde se ven los productos registrados

   if request.method == 'POST':

      form = FormProducto(request.POST)

      if form.is_valid():

         producto = Producto.objects.create(

         empresa_id = Empresa.objects.get(id=empresa_id),
         nombre = form.cleaned_data['nombre'],
         c_v_u = form.cleaned_data['c_v_u'], 
         p_v_u = form.cleaned_data['p_v_u'],
         participacion_ventas = form.cleaned_data['participacion_ventas'])

         
         producto.save()
         messages.success(request, 'producto añadido correctamente')

      else:
         print(form.errors)
         if(not form.errors):
            messages.success(request, 'Producto ya registrado')
         
         # raise ValidationError(('Producto ya se encuentra registrado'))


   productos = Producto.objects.filter(empresa_id=empresa_id)

   form = FormProducto()

   return render(request, "gestion_producto.html", {"productos": productos,'form':form})

def eliminar_producto(request, producto_id):
   producto = Producto.objects.get(empresa_id = 1,id = producto_id) 
   producto.delete()
   
   return redirect('http://127.0.0.1:8000/productos/')

def editar_producto(request, producto_id):


   producto = Producto.objects.get(id = producto_id)


   if request.method == 'GET':

      formConcepto = FormConcepto()

      form = FormProducto(instance=producto)

      conceptos = Concepto.objects.filter(producto_id=producto_id)
   
   elif request.method == 'POST':

      form = FormProducto(request.POST)

      if form.is_valid():

         producto.nombre = form.cleaned_data['nombre']
         producto.c_v_u = form.cleaned_data['c_v_u'] 
         producto.p_v_u = form.cleaned_data['p_v_u']
         producto.participacion_ventas = form.cleaned_data['participacion_ventas']

         producto.save()

   return render(request, "editar_producto.html",{"producto":producto,'form':form,'formConcepto':formConcepto,'conceptos':conceptos})

def añadir_concepto(request, producto_id):


   if request.method == 'POST':

      form = FormConcepto(request.POST)


      if form.is_valid():

         concepto = form.save(commit=False)

         concepto.producto_id = Producto.objects.get(id = producto_id)

         concepto.save()

   return redirect(f'http://127.0.0.1:8000/productos/gestion/editar/{producto_id}')


         




         



   