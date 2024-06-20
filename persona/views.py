from django.shortcuts import render, redirect

from .models import Persona
from .forms import DatosPersonaForm

def inicio(request):
     return render(request,'persona/index.html')
#     return HttpResponse('Bienvenidos a mi inicio!')

def datos_persona(request):
    formulario = DatosPersonaForm()

    if request.method == 'POST':
        formulario = DatosPersonaForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            edad = formulario.cleaned_data['edad']
            # Procesar los datos como desees, por ejemplo, guardarlos en la base de datos
            persona = Persona(nombre=nombre, edad=edad)
            persona.save()
            return redirect('inicio')  # Redirige a la página de inicio después de procesar el formulario

    return render(request, 'persona/datos_persona.html', {'formulario': formulario})



def lista_persona(request):
    personas = Persona.objects.all()  
    return render(request, 'persona/lista_personas.html', {'personas': personas})