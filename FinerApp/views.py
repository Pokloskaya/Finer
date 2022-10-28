from re import A
from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Empresa, FormConcepto, Producto,FormProducto,Concepto,FormEmpresa, Costos,FormCostos

# Create your views here.
def home(request):
   return render(request, "home.html")

def gestion_producto(request,empresa_id=1):

   
   

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
   producto = Producto.objects.get(empresa_id = 1,id = producto_id) 
   producto.delete()
   
def eliminar_costo(request, costo_id):
   
   costo = Costos.objects.get(empresa_id = 1,id = costo_id) 
   costo.delete()
   
   
   
   return redirect("/costosfijos")

def editar_producto(request,producto_id,empresa_id=1):
   
      
   tipoEmpresa = Empresa.objects.get(id=empresa_id).tipo_empresa
   
   producto = Producto.objects.get(id = producto_id)
   

   
   
   data = {"producto":producto,'tipoEmpresa':tipoEmpresa}
   
   
   if request.method == 'GET':
      
      if tipoEmpresa == 'productor':
         
         conceptos = Concepto.objects.filter(producto_id=producto_id)
         
         formConcepto = FormConcepto()        
         
         data['conceptos'] = conceptos
         data['formConcepto'] = formConcepto
      
      
   elif request.method == 'POST':

      form = FormProducto(request.POST)

      if form.is_valid():

         producto.nombre = form.cleaned_data['nombre']
         producto.c_v_u = form.cleaned_data['c_v_u'] 
         producto.p_v_u = form.cleaned_data['p_v_u']
         producto.participacion_ventas = form.cleaned_data['participacion_ventas']

         producto.save()
         
   data['form'] = FormProducto(instance=producto)
      
      
               

   return render(request, "editar_producto.html",data)

def añadir_concepto(request, producto_id):


   if request.method == 'POST':

      form = FormConcepto(request.POST)


      if form.is_valid():

         concepto = form.save(commit=False)

         concepto.producto_id = Producto.objects.get(id = producto_id)

         concepto.save()

   return redirect(f'/productos/editar/{producto_id}')

def registro(request):
       data = {'form': FormEmpresa()}
       if request.method == 'POST':
              formulario = FormEmpresa(request.POST)
              if formulario.is_valid():
                  formulario.save()
              
              
       return render(request, "registro.html",data)


def costos_fijos(request,empresa_id=1):

      
   if request.method == 'POST':
      
      
      costo = FormCostos(request.POST)
      
      
      if costo.is_valid():
         
         
         costo = costo.save(commit=False)
         
         costo.empresa_id = Empresa.objects.get(id=empresa_id)
         
         
         costo.save()
   
         
   costos = Costos.objects.filter(empresa_id=empresa_id)
   formCostos = FormCostos()
         
      
   
   return render(request,"costosfijos.html",{'costos':costos,'formCostos':formCostos})


         




         



   