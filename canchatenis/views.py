from django.shortcuts import render
from django.views.generic import ListView
from canchatenis.models import Entrenamientos
from canchatenis.models import Jugadores
from canchatenis.forms import JugadoresFormulario
# Create your views here.
def inicio(request):
    return render(request, 'canchatenis/index.html')

def profesores(request):
    return render(request, 'canchatenis/profesores.html')

def entrenamientos(request):
    return render(request, 'canchatenis/entrenamientos.html')

def jugadores(request):
    return render (request, "canchatenis/jugadores.html")

def fisico(request):
    return render (request, 'canchatenis/fisico.html')

def jugadoresformulario(request):
    if request.method == "POST":
        miFormulario = Jugadores(request.POST) # Aqui me llega la informacion del html
            # print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            jugador = Jugadores (nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"],)
            jugador.save()
            return render(request, "canchatenis/index.html")
    else:
            miFormulario = JugadoresFormulario()

    return render(request, "canchatenis/jugadoresformulario.html", {"miFormulario": miFormulario})

class EntrenamientosListview(ListView):
    model = Entrenamientos
    context_object_name = "entrenamientos"
    template_name = "canchatenis/listar.html"