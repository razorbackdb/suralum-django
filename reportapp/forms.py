from django import forms
from django.forms.widgets import MultiWidget, Widget
from tempus_dominus.widgets import DatePicker
import datetime


class DescForm(forms.Form):
    opciones = [('1', 'Ventas Totales'),
                ('2', 'Producto mas Vendido'),
                ('3', 'Ventas por Familia'),
                ('4', 'Ventas Suralum'),
                ('5', 'Ventas Huracan'),
                ('6', 'Ventas Industrial')]
    Descriptores = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=opciones)


class DateForm(forms.Form):
    YEAR_CHOICES = []
    for r in range(2010, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))
    Fecha = forms.ChoiceField(widget=forms.Select, choices=YEAR_CHOICES)
    #Fecha = forms.DateField(widget=DatePicker(attrs={'class' : 'datePicker'}))
