from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Empresa, FormConcepto, Producto,FormProducto,Concepto

# Create your views here.
def home(request):
   return render(request, "home.html")

def gestion_producto(request,empresa_id=2):

   
   

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


   productos = Producto.objects.filter(empresa_id=empresa_id)

   form = FormProducto()

   return render(request, "gestion_producto.html", {"productos": productos,'form':form,'tipoEmpresa':Empresa.objects.get(id=empresa_id).tipo_empresa})

def eliminar_producto(request, producto_id):
   producto = Producto.objects.get(empresa_id = 2,id = producto_id) 
   producto.delete()
   
   return redirect('http://127.0.0.1:8000/productos/')

def editar_producto(request,producto_id,empresa_id=2):


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

   return render(request, "editar_producto.html",{"producto":producto,'form':form,'formConcepto':formConcepto,'conceptos':conceptos,'tipoEmpresa':Empresa.objects.get(id=empresa_id).tipo_empresa})

def añadir_concepto(request, producto_id):


   if request.method == 'POST':

      form = FormConcepto(request.POST)


      if form.is_valid():

         concepto = form.save(commit=False)

         concepto.producto_id = Producto.objects.get(id = producto_id)

         concepto.save()

   return redirect(f'http://127.0.0.1:8000/productos/gestion/editar/{producto_id}')


         




         



   