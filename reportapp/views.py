from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

from reportapp.models import Familia, Productos, Ventas

from .forms import DateForm, DescForm

# Create your views here.


@login_required
def index(request):
    #descriptores = request.session['descriptores']
    descriptores = {'1', '2', '3', '4', '5', '6'}
    #fechas = request.session['fechas']
    fechas = {'2016', '2017', '2018', '2019', '2020'}
    x = {}
    for f in fechas:
        subtotal = []
        productos_mas_vendidos = []
        ventas_por_familia = []
        suralum_productos = []
        suralum_total = 0
        huracan_productos = []
        huracan_total = 0
        industrial_productos = []
        industrial_total = 0
        total = 0
        if '1' in descriptores:
            ventas_por_mes = Ventas.objects.annotate(month=TruncMonth('fecha')).using('suralum').values(
                'month').annotate(total_mensual=Sum('subtotal')).filter(fecha__year=f).order_by('month').values_list('total_mensual')
            for p in ventas_por_mes:
                subtotal.append(p[0])
                total = total + p[0]
        if '2' in descriptores:
            productos = Productos.objects.using('suralum').raw('''SELECT productos.id_producto, productos.descripcion, SUM(venta_productos.cantidad*venta_productos.precio) as t
                                                                        FROM productos JOIN venta_productos ON(venta_productos.id_producto=productos.id_producto) JOIN ventas ON(ventas.id_venta=venta_productos.id_venta) 
                                                                        WHERE EXTRACT(YEAR FROM ventas.fecha)=%s
                                                                        GROUP BY productos.id_producto, productos.descripcion
                                                                        ORDER BY t DESC;''', [f])[:10]
            for p in productos:
                productos_mas_vendidos.append(
                    [p.id_producto, p.descripcion, p.t])

        if '3' in descriptores:
            familias = Familia.objects.using('suralum').raw('''SELECT familia.id_familia, familia.descripcion_familia, SUM(venta_productos.cantidad*venta_productos.precio) as t
                                                                    FROM familia JOIN productos ON familia.id_familia = productos.id_familia
                                                                    JOIN venta_productos ON venta_productos.id_producto = productos.id_producto 
                                                                    JOIN ventas ON venta_productos.id_venta=ventas.id_venta
                                                                    WHERE EXTRACT(YEAR FROM ventas.fecha) = %s
                                                                    GROUP BY familia.id_familia, familia.descripcion_familia;''', [f])
            for p in familias:
                ventas_por_familia.append([p.descripcion_familia, p.t])
        if '4' in descriptores:
            suralum = Productos.objects.using('suralum').raw('''SELECT productos.id_producto, productos.descripcion, SUM(venta_productos.cantidad*venta_productos.precio) as t
                                                                    FROM familia JOIN productos ON familia.id_familia = productos.id_familia
                                                                    JOIN venta_productos ON venta_productos.id_producto = productos.id_producto 
                                                                    JOIN ventas ON venta_productos.id_venta=ventas.id_venta
                                                                    WHERE EXTRACT(YEAR FROM ventas.fecha) = %s AND familia.id_familia = 1
                                                                    GROUP BY productos.id_producto, productos.descripcion
                                                                    ORDER BY t DESC;''', [f])
            for p in suralum:
                suralum_total = suralum_total + p.t
            for p in suralum[:10]:
                suralum_productos.append(
                    [p.id_producto, p.descripcion, p.t])
        if '5' in descriptores:
            huracan = Productos.objects.using('suralum').raw('''SELECT productos.id_producto, productos.descripcion, SUM(venta_productos.cantidad*venta_productos.precio) as t
                                                                    FROM familia JOIN productos ON familia.id_familia = productos.id_familia
                                                                    JOIN venta_productos ON venta_productos.id_producto = productos.id_producto 
                                                                    JOIN ventas ON venta_productos.id_venta=ventas.id_venta
                                                                    WHERE EXTRACT(YEAR FROM ventas.fecha) = %s AND familia.id_familia = 2
                                                                    GROUP BY productos.id_producto, productos.descripcion
                                                                    ORDER BY t DESC;''', [f])
            for p in huracan:
                huracan_total = huracan_total + p.t
            for p in huracan[:10]:
                huracan_productos.append(
                    [p.id_producto, p.descripcion, p.t])
        if '6' in descriptores:
            industrial = Productos.objects.using('suralum').raw('''SELECT productos.id_producto, productos.descripcion, SUM(venta_productos.cantidad*venta_productos.precio) as t
                                                                    FROM familia JOIN productos ON familia.id_familia = productos.id_familia
                                                                    JOIN venta_productos ON venta_productos.id_producto = productos.id_producto 
                                                                    JOIN ventas ON venta_productos.id_venta=ventas.id_venta
                                                                    WHERE EXTRACT(YEAR FROM ventas.fecha) = %s AND familia.id_familia = 3
                                                                    GROUP BY productos.id_producto, productos.descripcion
                                                                    ORDER BY t DESC;''', [f])
            for p in industrial:
                industrial_total = industrial_total + p.t
            for p in industrial[:10]:
                industrial_productos.append(
                    [p.id_producto, p.descripcion, p.t])
        x[f] = {
            'total': total,
            'ventas_por_mes': subtotal,
            'productos_mas_vendidos': productos_mas_vendidos,
            'ventas_por_familia': ventas_por_familia,
            'suralum_productos': suralum_productos,
            'suralum_total': suralum_total,
            'huracan_productos': huracan_productos,
            'huracan_total': huracan_total,
            'industrial_productos': industrial_productos,
            'industrial_total': industrial_total

        }
    print(x)

    return render(request, 'index.html', {'datos': x, 'descriptores': descriptores})


@login_required
def report(request):
    # if this is a POST request we need to process the form data
    dateformset = formset_factory(DateForm)
    if 'descriptores' in request.session.keys():
        del request.session['descriptores']
    if 'fechas' in request.session.keys():
        del request.session['fechas']
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        descform = DescForm(request.POST)
        dateform = dateformset(request.POST)
        # check whether it's valid:
        if descform.is_valid() and dateform.is_valid():
            request.session['descriptores'] = descform.cleaned_data['Descriptores']

            fechas = []
            for f in dateform.data:
                if f[7:] == "Fecha":
                    fechas.append(dateform.data[f])
            request.session['fechas'] = fechas
            return HttpResponseRedirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        descform = DescForm()
        dateform = dateformset
    return render(request, 'report.html', {'descform': descform, 'dateform': dateform})


@login_required
def table(request):
    return render(request, 'table.html')
