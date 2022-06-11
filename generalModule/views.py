from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def productos_por_categoria(request):
    with connection.cursor() as cursor:
        query = """
            select
                PC.nombre_categoria,
                count(Productos.id) as conteo
            from ProductoCategorias PC
            left join Productos on Productos.categoria_id = PC.id
            group by PC.id;
        """
        cursor.execute(query)
        data = cursor.fetchall()

    contexto = {'data': data}

    return render(request, 'productos_por_categoria.html', context=contexto)


@login_required
def costos_totales_por_categoria(request):
    with connection.cursor() as cursor:
        query = """
            select
                PC.nombre_categoria,
                coalesce(sum(P.precio), 0) as total
            from ProductoCategorias PC
            left join Productos P on PC.id = P.categoria_id
            group by PC.id;
        """
        cursor.execute(query)
        data = cursor.fetchall()

    contexto = {'data': data}
    return render(request, 'costos_totales_por_categoria.html', context=contexto)


@login_required
def compras_a_proveedores(request):
    with connection.cursor() as cursor:
        query = """
            select
                Proveedores.nombre_proveedor,
                coalesce(count(GC.id), 0) as conteo_compras,
                coalesce(sum(GC.valor), 0) as total_compras
            from Proveedores
            left join GestionCompras GC on Proveedores.id = GC.proveedor_id
            group by Proveedores.id;
        """
        cursor.execute(query)
        data = cursor.fetchall()

    contexto = {'data': data}
    return render(request, 'compras_a_proveedores.html', context=contexto)


@login_required
def detalles_compras_a_proveedores(request):
    with connection.cursor() as cursor:
        query = """
            select
                Proveedores.nombre_proveedor,
                Gc.valor as valor_compra,
                P.nombre_producto
            from Proveedores
            inner join GestionCompras GC on Proveedores.id = GC.proveedor_id
            inner join Productos P on GC.producto_id = P.id;
        """
        cursor.execute(query)
        data = cursor.fetchall()

    contexto = {'data': data}
    return render(request, 'detalle_compras_a_proveedores.html', context=contexto)


@login_required
def promedio_costo_actividades_por_molino(request):
    with connection.cursor() as cursor:
        query = """
            select
                Molinos.nombre_molino,
                avg(O.costo) as costo_promedio_de_ordenes
            from Molinos
            inner join Ordenes O on Molinos.id = O.molino_id
            group by Molinos.id;
        """
        cursor.execute(query)
        data = cursor.fetchall()

    contexto = {'data': data}
    return render(request, 'promedio_costo_actividades_por_molino.html', context=contexto)


@login_required
def detalle_costo_actividad_por_molino(request):
    with connection.cursor() as cursor:
        query = """
            select
                Molinos.nombre_molino,
                A.nombre_actividad,
                O.costo
            from Molinos
            inner join Ordenes O on Molinos.id = O.molino_id
            inner join Actividades A on O.actividad_id = A.id
            order by nombre_molino;
        """
        cursor.execute(query)
        data = cursor.fetchall()

    contexto = {'data': data}
    return render(request, 'detalle_costo_actividad_por_molino.html', context=contexto)


@login_required
def costo_promedio_personal_por_cargo(request):
    with connection.cursor() as cursor:
        query = """
            select
                Cargo.nombre_cargo,
                '$ ' || (AVG(P.sueldo_hora) * 8 * 30) as sueldo_promedio_por_mes
            from Cargo
            inner join Personal P on Cargo.id = P.cargo_id
            group by Cargo.id;
        """
        cursor.execute(query)
        data = cursor.fetchall()

    contexto = {'data': data}
    return render(request, 'costo_promedio_personal_por_cargo.html', context=contexto)
