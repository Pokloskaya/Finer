from email.policy import default
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
   c_v_u = models.DecimalField(max_digits=10,decimal_places=3,default=0,blank=True)  # Esto se puede calcular con base en el costo de los conceptos asociados 
   p_v_u = models.DecimalField(max_digits=10,decimal_places=3)
   participacion_ventas = models.DecimalField(max_digits=10,decimal_places=3)
   margen_contribucion = models.DecimalField(max_digits=10,decimal_places=3,default=0)
   
   
class Concepto(models.Model):
   producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=True)
   nombreConcepto = models.CharField(max_length=50) 
   unidad_compra = models.CharField(max_length=30)
   precio_compra = models.DecimalField(max_digits=10,decimal_places=3)
   unidad_ultilizada = models.DecimalField(max_digits=10,decimal_places=3,default=0)
   factor = models.DecimalField(max_digits=10,decimal_places=3,default=0)
   costo_variable = models.DecimalField(max_digits=10,decimal_places=3,default=0)


   

      
class Costos(models.Model):
   empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE) #Llave foranea 
   nombreCosto = models.CharField(max_length=50)
   valorCosto = models.DecimalField(max_digits=10,decimal_places=1)
      
