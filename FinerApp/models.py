from django.db import models
from django import forms
from django.core.exceptions import ValidationError

from . import choices

class Empresa(models.Model):

   nombre = models.CharField(max_length=50)
   contraseña = models.CharField(max_length=20)
   tipo_empresa = models.CharField(max_length=20,choices=choices.TIPO_EMPRESAS) #Llave foranea
   margen_contribucion_negocio = models.DecimalField(max_digits=10,decimal_places=3,default=0)
         
class Producto(models.Model):
   empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE) #Llave foranea 

   nombre = models.CharField(max_length=30, unique=True) #  unique=True

   c_v_u = models.DecimalField(max_digits=10,decimal_places=1)  # Esto se puede calcular con base en el costo de los conceptos asociados 
   p_v_u = models.DecimalField(max_digits=10,decimal_places=1)
   participacion_ventas = models.DecimalField(max_digits=10,decimal_places=1)
   margen_contribucion = models.DecimalField(max_digits=10,decimal_places=1,default=0)
   

class Concepto(models.Model):
   producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=True)
   nombreConcepto = models.CharField(max_length=50) 
   unidad_compra = models.CharField(max_length=30)
   precio_compra = models.DecimalField(max_digits=10,decimal_places=1)
   unidad_ultilizada = models.DecimalField(max_digits=10,decimal_places=1,default=0)
   factor = models.DecimalField(max_digits=10,decimal_places=1,default=0)
   costo_variable = models.DecimalField(max_digits=10,decimal_places=1,default=0)

class Costos(models.Model):
   empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE) #Llave foranea 
   nombreCosto = models.CharField(max_length=50)
   valorCosto = models.DecimalField(max_digits=10,decimal_places=1)

#------------------------------------------------------------------------------------------------------------------------------
class FormProducto(forms.ModelForm):

   class Meta:
      model = Producto

      fields = [
         'nombre',
         'c_v_u',
         'p_v_u',
         'participacion_ventas',
      ]

      labels = { #el nombre que se le va a mostrar al usuario
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

      # def verificarDatos(self):
      #       nombre = self.cleaned_data('nombre')

      #       if Producto.objects.filter(nombre__iexact=nombre).exists(): #si el nombre se encuentra ya ingresado
      #          raise models.ValidationError('Producto ya se encuentra registrado')
      #       return nombre


class FormConcepto(forms.ModelForm):

   class Meta:
      model = Concepto

      fields = [
         'nombreConcepto',
         'unidad_compra',
         'precio_compra',
         'unidad_ultilizada',
         'factor',
         'costo_variable',
      ]

      labels = {
         'nombreConcepto': 'Nombre',
         'unidad_compra': 'Unidad de compra',
         'precio_compra': 'Precio de compra',
         'unidad_ultilizada': 'Unidad Ultilizada',
         'factor': 'factor',
         'costo_variable':'Costo variable',
      }

      widgets = {
         'nombreConcepto':forms.TextInput(attrs={'class':'form-control','placeholder':labels['nombreConcepto']}),
         'unidad_compra':forms.TextInput(attrs={'class':'form-control','placeholder':labels['unidad_compra']}),
         'precio_compra': forms.TextInput(attrs={'class':'form-control','placeholder':labels['precio_compra']}),
         'unidad_ultilizada': forms.TextInput(attrs={'class':'form-control','placeholder':labels['unidad_ultilizada']}),
         'factor': forms.TextInput(attrs={'class':'form-control','placeholder':labels['factor']}),
         'costo_variable': forms.TextInput(attrs={'class':'form-control','placeholder':labels['costo_variable']}),
      }

class FormCostos(forms.ModelForm):
      class Meta:
         model = Costos

         fields = [
            'nombreCosto',
            'valorCosto',
         ]

         labels = {
            'nombreCosto': 'costo',
            'valorCosto': 'valor del costo',
         }

         widgets = {
            'nombreCosto':forms.TextInput(attrs={'class':'form-control','placeholder':labels['nombreCosto']}),
            'valorCosto':forms.TextInput(attrs={'class':'form-control','placeholder':labels['valorCosto']}),
         }