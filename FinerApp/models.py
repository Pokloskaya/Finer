from django.db import models
from django import forms


from . import choices

class Empresa(models.Model):

   nombre = models.CharField(max_length=50)
   contraseña = models.CharField(max_length=20)
   tipo_empresa = models.CharField(max_length=20,choices=choices.TIPO_EMPRESAS) #Llave foranea
   margen_contribucion_negocio = models.DecimalField(max_digits=10,decimal_places=3,default=0)
      
class Producto(models.Model):
   empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE) #Llave foranea 
   nombre = models.CharField(max_length=30)
   c_v_u = models.DecimalField(max_digits=10,decimal_places=3)  # Esto se puede calcular con base en el costo de los conceptos asociados 
   p_v_u = models.DecimalField(max_digits=10,decimal_places=3)
   participacion_ventas = models.DecimalField(max_digits=10,decimal_places=3)
   margen_contribucion = models.DecimalField(max_digits=10,decimal_places=3,default=0)
   
   
class Concepto(models.Model):
   producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=True)
   nombre = models.CharField(max_length=50) 
   unidad_compra = models.CharField(max_length=30)
   precio_compra = models.DecimalField(max_digits=10,decimal_places=3)
   tipo_unidad  = models.CharField(max_length=30)
   unidad = models.DecimalField(max_digits=10,decimal_places=3,default=0)
   factor = models.DecimalField(max_digits=10,decimal_places=3,default=0)
   costo_variable = models.DecimalField(max_digits=10,decimal_places=3,default=0)

   
class FormProducto(forms.ModelForm):

   class Meta:
      model = Producto

      fields = [
         'nombre',
         'c_v_u',
         'p_v_u',
         'participacion_ventas',
      ]

      labels = {
         'nombre': 'Nombre',
         'c_v_u': 'Costo variable unitario',
         'p_v_u': 'Precio variable unitario',
         'participacion_ventas':'Participacion ventas'
      }

      widgets = {
         'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':labels['nombre']}),
         'c_v_u':forms.TextInput(attrs={'class':'form-control','placeholder':labels['c_v_u']}),
         'p_v_u': forms.TextInput(attrs={'class':'form-control','placeholder':labels['p_v_u']}),
         'participacion_ventas': forms.TextInput(attrs={'class':'form-control','placeholder':labels['participacion_ventas']}),
         
      }
