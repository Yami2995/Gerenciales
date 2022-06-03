from django.contrib import admin
from django.contrib.admin import ModelAdmin
from generalModule import models


@admin.register(models.Actividad)
class ActividadAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Equipo)
class EquipoAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Etapa)
class EtapaAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.LineaRuta)
class LineaRuta(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Molino)
class MolinoAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Orden)
class OrdenAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Personal)
class PersonalAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Presupuesto)
class PresupuestoAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Producto)
class ProductoAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Proveedor)
class ProveedorAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.CategoriaProducto)
class CategoriaProductoAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.PersonalCategoria)
class PersonalCategoriaAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.Cargo)
class CargoAdmin(ModelAdmin):
    readonly_fields = ['id']


@admin.register(models.GestionCompra)
class GestionCompraAdmin(ModelAdmin):
    readonly_fields = ['id']
