from django.shortcuts import render
from django.views.generic import ListView
from canchatenis.models import Entrenamientos
from canchatenis.models import Jugadores
from canchatenis.forms import JugadoresFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def inicio(request):
    return render(request, 'canchatenis/index.html')

@login_required

def about(request):
    return render(request, 'canchatenis/about.html')

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

class EntrenamientosListview(LoginRequiredMixin,ListView):
    model = Entrenamientos
    context_object_name = "entrenamientos"
    template_name = "canchatenis/listar.html"

from canchatenis.forms import BuscaEntrenamientoForm

def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaEntrenamientoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            entrenamientos = Entrenamientos.objects.filter(nombre__icontains=informacion["entrenamientos"])

            return render(request, "canchatenis/mostrar_entrenamientos.html", {"entrenamientos": entrenamientos})
    else:
        mi_formulario = BuscaEntrenamientoForm()

    return render(request, "canchatenis/buscar_form_con_api.html", {"mi_formulario": mi_formulario})