from django import forms


class DatosPersonaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    edad = forms.IntegerField(label='Edad')