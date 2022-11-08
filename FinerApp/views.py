from re import A
from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Empresa, Producto,Concepto, Costos, Cfu
from .forms import FormEmpresa,FormCostos,FormConcepto,FormProducto, FormCfu

# Create your views here.
def home(request):
   return render(request, "home.html")

def gestion_producto(request,empresa_id=1):

   tipoEmpresa = Empresa.objects.get(id=empresa_id).tipo_empresa
   
   if request.method == 'POST':

      form = FormProducto(request.POST)

      if form.is_valid():   
         c_v_U = form.cleaned_data['c_v_u']
         
      
         if tipoEmpresa == "productor":
            c_v_U = 0

         producto = Producto.objects.create(
         
         empresa_id = Empresa.objects.get(id=empresa_id),
         nombre = form.cleaned_data['nombre'],
         c_v_u = c_v_U,
         p_v_u = form.cleaned_data['p_v_u'],
         participacion_ventas = form.cleaned_data['participacion_ventas'])

         producto.save()


   productos = Producto.objects.filter(empresa_id=empresa_id)
   form = FormProducto()

   return render(request, "gestion_producto.html", {"productos": productos,'form':form,'tipoEmpresa':Empresa.objects.get(id=empresa_id).tipo_empresa})

#----------------------------------------------------------------------------------------------------

def obtenerDiasLaborados():
       
   prueba = Cfu.objects.values_list('diasLaboradosAnuales', flat=True)
   
   return prueba


def indicadores(request, empresa_id=1):

   #--------------------------------------------------------
   if request.method == 'POST':
    
      form = FormCfu(request.POST)

      if form.is_valid():
         form.save()
         return redirect("/indicadores")
      else:
         print(form.errors)
         

   form = FormCfu()
   prueba = obtenerDiasLaborados()
   total = sum(prueba)
   return render(request, "indicadores.html", {'prueba':total, 'form':form})

#----------------------------------------------------------------------------------------------------------------------


def eliminar_producto(request, producto_id):
   producto = Producto.objects.get(empresa_id = 1,id = producto_id) 
   producto.delete()
   
   return redirect("/productos")
   
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
      if form.has_changed() and form.is_valid():
         
         if tipoEmpresa == 'productor':
            c_v_u = 0
         elif tipoEmpresa == 'comerciante':
            c_v_u = form.cleaned_data['c_v_u']
          
         producto.nombre = form.cleaned_data['nombre']
         producto.c_v_u = c_v_u
         producto.p_v_u = form.cleaned_data['p_v_u']
         producto.participacion_ventas = form.cleaned_data['participacion_ventas']
         producto.save()
         
      return redirect(f"/productos/editar/{producto_id}")
         
   data['form'] = FormProducto(instance=producto)

   return render(request, "editar_producto.html",data)

def añadir_concepto(request, producto_id):
   if request.method == 'POST':
      form = FormConcepto(request.POST)

      if form.is_valid():
         concepto = form.save(commit=False)
         concepto.producto_id = Producto.objects.get(id = producto_id)
         concepto.save()
      else:
         print(form.errors)

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
   sumCostos = obtenerCostoTotalEmpresa()
   formCostos = FormCostos()
   
   return render(request,"costosfijos.html",{'costos':costos,'formCostos':formCostos,'costosTotales':sumCostos})

def eliminar_concepto(request,concepto_id):
   
   concepto = Concepto.objects.get(id=concepto_id)
   productoid = concepto.producto_id.empresa_id
   concepto.delete()
   
   return redirect(f"/productos/editar/{productoid}")


def obtenerCostoTotalEmpresa():
   amounts = Costos.objects.values_list('valorCosto', flat=True)
   total = sum(amounts)
   
   return total





   
   
   


         




         



   