from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Vivienda, LNPatron
from .forms import ConsultaForm

def consulta_view(request):
    form = ConsultaForm()
    resultados = None
    error = None

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = str( form.cleaned_data['consulta'] ).lower()
            patrones = LNPatron.objects.all()

            for patron in patrones:
                if patron.patron in consulta:
                    sql = patron.consultasql
                    viviendas = Vivienda.objects.raw(sql)
                    resultados = viviendas
                    break
            else:
                error = "No se encontraron resultados para la consulta."

    return render(request, 'viviendas/consulta.html', {
        'form': form,
        'resultados': resultados,
        'error': error
    })
