from django import forms

class ConsultaForm(forms.Form):
    consulta = forms.CharField(label='Ingrese su consulta', max_length=255)

