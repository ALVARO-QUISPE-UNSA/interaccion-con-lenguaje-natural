from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Vivienda, LNPatron
from .forms import ConsultaForm

def consulta_view(request):
    form = ConsultaForm()
    resultados = None
    error = None

    #if request.method == 'POST':
    #    form = ConsultaForm(request.POST)
    #    if form.is_valid():
    #        sql = make_query(str( form.cleaned_data['consulta'] ).lower())
    #        viviendas = Vivienda.objects.raw(sql)

    return render(request, 'viviendas/consulta.html', {
        'form': form,
        'resultados': resultados,
        'error': error
    })

def make_query(str: str) -> str:

    return ""
