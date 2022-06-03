from django.urls import path

from generalModule import views

urlpatterns = [
    path('productos-por-categoria/', views.productos_por_categoria, name='productos_por_categoria'),
    path('costos-totales-por-categoria/', views.costos_totales_por_categoria, name='costos_por_categoria'),
    path('compras-a-proveedores/', views.compras_a_proveedores, name='compras_a_proveedores'),
    path('compras-a-proveedores-detalle/', views.detalles_compras_a_proveedores, name='detalle_compras_a_proveedores'),
    path('promedio-costo-actividades-por-molino/', views.promedio_costo_actividades_por_molino, name='promedio_costo_actividades_molino'),
    path('detalle-costo-actividades-por-molino/', views.detalle_costo_actividad_por_molino, name='detalle_costo_activides_molino'),
    path('costo-promedio-personal-por-cargo/', views.costo_promedio_personal_por_cargo, name='costo_promedio_personal_por_cargo'),
]
