from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name= 'home'), 
    path('productos/', views.gestion_producto, name= 'gestion_producto'),
    path('productos/eliminar/<producto_id>', views.eliminar_producto, name = 'eliminar_producto'),
    path('productos/gestion/editar/<producto_id>', views.editar_producto, name = 'editar_producto'), 
    path('productos/producto_productor', views.producto_productor, name = 'producto_productor'), 
]

 