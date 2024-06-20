from django.shortcuts import render
from django.http import HttpResponse
#V1

def inicio(request):
     return render(request,'persona/index.html')
#     return HttpResponse('Bienvenidos a mi inicio!')



from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'persona/lista_personas.html', {'personas': personas})

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'persona/crear_persona.html', {'form': form})

def detalle_persona(request, pk):
    persona = Persona.objects.get(pk=pk)
    return render(request, 'persona/detalle_persona.html', {'persona': persona})

def editar_persona(request, pk):
    persona = Persona.objects.get(pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('detalle_persona', pk=pk)
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'persona/editar_persona.html', {'form': form, 'persona': persona})

def eliminar_persona(request, pk):
    persona = Persona.objects.get(pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('lista_personas')
    return render(request, 'persona/confirmar_eliminar_persona.html', {'persona': persona})


