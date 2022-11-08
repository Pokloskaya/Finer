from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name= 'home'), 
    path('registro/', views.registro , name= 'registro'), 
    path('indicadores', views.indicadores , name= 'indicadores'), 
    path('productos/', views.gestion_producto, name= 'gestion_producto'),
    path('productos/eliminar/<producto_id>', views.eliminar_producto, name = 'eliminar_producto'),
    path('productos/editar/<producto_id>', views.editar_producto, name = 'editar_producto'),
    path('productos/editar/<producto_id>/añadir_concepto',views.añadir_concepto,name='añadir_concepto'),
    path('costosfijos/',views.costos_fijos,name="costos_fijos"),
    path('eliminarcosto/<costo_id>',views.eliminar_costo,name="eliminar_costo"),
    path('productos/eliminarConcepto/<concepto_id>',views.eliminar_concepto,name="eliminar_concepto")
]
 