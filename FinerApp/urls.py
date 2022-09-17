from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name= 'home'), 
    path('productos/gestion/', views.gestion_producto, name= 'gestion_producto'),
    path('productos/gestion/agregar/', views.agregar_producto, name= 'agregar_producto'),
    path('productos/gestion/eliminar/<producto_id>', views.eliminar_producto, name = 'eliminar_producto'),
    path('productos/gestion/editar/<producto_id>', views.editar_producto, name = 'editar_producto'),
    
]
 