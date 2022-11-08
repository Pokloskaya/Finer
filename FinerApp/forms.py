import imp
# from django.contrib import admin

from .models import Producto,Concepto,Costos,Empresa, Cfu
from django import forms

#  admin.site.register(Costos)
#  admin.site.register(Cfu)
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
      

class FormEmpresa(forms.ModelForm):
   class Meta:
      model = Empresa
      
      fields = ['nombre', 'contraseña', 'tipo_empresa']
      
class FormCostos(forms.ModelForm):
    
    
      class Meta:
         model = Costos

         fields = [
            'nombreCosto',
            'valorCosto',
         ]

         labels = {
            'nombreCosto': 'Nombre del costo',
            'valorCosto': 'Valor',
         }

         widgets = {
            'nombreCosto':forms.TextInput(attrs={'class':'form-control','placeholder':labels['nombreCosto']}),
            'valorCosto':forms.TextInput(attrs={'class':'form-control','placeholder':labels['valorCosto']}),
         }

class FormCfu(forms.ModelForm):
      class Meta:
         model = Cfu

         fields = [
            'diasLaboradosAnuales',
            'jornadaDiara',
            'empleadosParticipacion',
         ]

         labels = {
            'diasLaboradosAnuales': 'dias laborados anualmente',
            'jornadaDiara': 'Jornada diaria',
            'empleadosParticipacion': 'Jornada real de trabajo diario',
         }

         widgets = {
            'diasLaboradosAnuales':forms.TextInput(attrs={'class':'form-control','placeholder':labels['diasLaboradosAnuales']}),
            'jornadaDiara':forms.TextInput(attrs={'class':'form-control','placeholder':labels['jornadaDiara']}),
            'empleadosParticipacion':forms.TextInput(attrs={'class':'form-control','placeholder':labels['empleadosParticipacion']}),
         }