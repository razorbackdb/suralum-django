from .forms import DateForm, DescForm
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reportapp.models import Ventas
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum

# Create your views here.

@login_required
def index(request):
    descriptores = request.session['descriptores']
    fechas = request.session['fechas']
    if '1' in descriptores:
        subtotal = []
        total = 0
        print(fechas)
        ventas_por_mes = Ventas.objects.annotate(month=TruncMonth('fecha')).using('suralum').values(
            'month').annotate(total_mensual=Sum('subtotal')).filter(fecha__year=fechas[0][:4]).order_by('month')
        for p in ventas_por_mes:
            subtotal.append(p['total_mensual'])
            total = total + p['total_mensual']
            print(p['month'], p['total_mensual'])
    return render(request, 'index.html', {'fechas': fechas, 'subtotal': subtotal, 'total': total})


@login_required
def table(request):
    return render(request, 'table.html')


@login_required
def report(request):
    # if this is a POST request we need to process the form data
    descformset = formset_factory(DescForm)
    dateformset = formset_factory(DateForm)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        descform = descformset(request.POST)
        dateform = dateformset(request.POST)
        # check whether it's valid:
        if descform.is_valid() and dateform.is_valid():
            descriptores = descform.data.getlist('form-0-Descriptores')
            request.session['descriptores'] = descriptores

            fechas = []

            for f in range(int(dateform.data.getlist('form-TOTAL_FORMS')[0])-1):
                fechas.append(dateform.data.getlist('form-'+str(f)+'-Fecha')[0])
            request.session['fechas'] = fechas
            return HttpResponseRedirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        if 'descriptores' in request.session.keys():
            del request.session['descriptores']
            del request.session['fechas']
        print(request.session.keys())
        descform = descformset
        dateform = dateformset

    return render(request, 'report.html', {'descform': descform, 'dateform': dateform})
