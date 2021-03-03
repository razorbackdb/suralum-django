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
    descriptores = request.session['descriptores']
    fechas = request.session['fechas']
    x = {}
    for f in fechas:
        subtotal = []
        productos_mas_vendidos = []
        ventas_por_familia = []
        total = 0
        print(f)
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
        x[f] = {
            'total' : total,
            'ventas_por_mes': subtotal,
            'productos_mas_vendidos': productos_mas_vendidos,
            'ventas_por_familia': ventas_por_familia
        }
    print(x)

    return render(request, 'index.html', { 'datos' : x })


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
            print(dateform.data)
            for f in dateform.data:
                if f[7:] == "Fecha":
                    fechas.append(dateform.data[f])
                print(f)
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