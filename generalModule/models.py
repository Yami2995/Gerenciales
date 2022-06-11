from django.db import models

# Create your models here.


class Actividad(models.Model):
    num_actividad = models.CharField(max_length=100)
    fechadoc = models.DateTimeField()
    fechazafra = models.ForeignKey('Presupuesto', on_delete=models.CASCADE)
    nombre_actividad = models.CharField(max_length=100)
    duracion = models.FloatField()

    def __str__(self):
        return self.nombre_actividad

    class Meta:
        db_table = 'Actividades'
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'


class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_equipo

    class Meta:
        db_table = 'Equipos'


class Etapa(models.Model):
    nombre_etapa = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_etapa

    class Meta:
        db_table = 'Etapas'


class LineaRuta(models.Model):
    nombre_linearuta = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_linearuta

    class Meta:
        db_table = 'LineaRutas'


class Molino(models.Model):
    nombre_molino = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_molino

    class Meta:
        db_table = 'Molinos'


class Orden(models.Model):
    costo = models.FloatField()

    # Relationships
    actividad = models.ForeignKey('Actividad', on_delete=models.CASCADE)
    etapa = models.ForeignKey('Etapa', on_delete=models.CASCADE)
    linea_ruta = models.ForeignKey('LineaRuta', on_delete=models.CASCADE)
    molino = models.ForeignKey('Molino', on_delete=models.CASCADE)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Ordenes'


class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9, null=True, blank=True)
    sueldo_hora = models.FloatField()

    # Relationships
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    categoria = models.ForeignKey('PersonalCategoria', on_delete=models.CASCADE)
    linea_ruta = models.ForeignKey('LineaRuta', on_delete=models.CASCADE)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Personal'


class Presupuesto(models.Model):
    nombre_presupuesto = models.CharField(max_length=100)
    presupuesto_inicial = models.FloatField()

    class Meta:
        db_table = 'Presupuestos'

    def __str__(self):
        return f'{self.nombre_presupuesto} - ${self.presupuesto_inicial:.2f}'


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio = models.FloatField()

    # Relationships
    categoria = models.ForeignKey('CategoriaProducto', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Productos'

    def __str__(self):
        return self.nombre_producto


class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        db_table = 'Proveedores'


class CategoriaProducto(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        db_table = 'ProductoCategorias'


class PersonalCategoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        db_table = 'PersonalCategoria'


class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cargo

    class Meta:
        db_table = 'Cargo'


class GestionCompra(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    fechaZafra = models.ForeignKey('Presupuesto', on_delete=models.CASCADE)

    cantidad = models.IntegerField()
    valor = models.FloatField()

    class Meta:
        db_table = 'GestionCompras'


class PermisosPersonalizados(models.Model):
    class Meta:
        db_table = 'PermisosPersonalizados'
        permissions = [
            ('usuario_estandar', 'Usuario estandar'),
            ('usuario_resumen', 'Usuario con reportes resumidos'),
            ('usuario_detalle', 'Usuario con reportes detallados')
        ]
