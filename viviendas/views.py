import re
from django.db.models import query
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import LNDiccionario, Vivienda, LNPatron
from .forms import ConsultaForm

def consulta_view(request):
    form = ConsultaForm()
    resultados = None
    error = None

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            sql_query = make_query(str(form.cleaned_data['consulta']).lower())
            if sql_query:
                print(f"\033[31m{sql_query}\033[0m")
                resultados = Vivienda.objects.raw(sql_query)
            else: 
                error = "No se encontraron resultados para la consulta"

    return render(request, 'viviendas/consulta.html', {
        'form': form,
        'resultados': resultados,
        'error': error
    })

def make_query(consulta: str) -> str:
    filtros = []
    for entry in LNDiccionario.objects.all():
        match = re.search(entry.patron, consulta)
        if not match: continue
        campo = entry.campo
        if entry.condicion:
            condicion = str( entry.condicion )
            if "%s" in condicion:
                condicion = condicion.replace("%s", match.group(1))
                filtros.append(f"{campo} {condicion}")
        else:
            valor = match.group(1)
            if campo == "ndormitorios":
                filtros.append(f"{campo} = {valor}")
            else: 
                filtros.append(f"{campo} = '{valor}'")

    if not filtros: return ""
    query = "SELECT * FROM viviendas WHERE " + "AND".join(filtros)
    return query
