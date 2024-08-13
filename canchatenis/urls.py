from django.urls import path
from canchatenis import views

urlpatterns = [
    path('', views.inicio ),
    path('fisico', views.fisico, name="fisico"),
    path('profesores', views.profesores, name="profesores"),
    path('entrenamientos', views.entrenamientos, name="entrenamientos"),
    path('listar', views.EntrenamientosListview.as_view(), name="listarentrenamientos"),
    path('jugadores', views.jugadores, name='jugadores'),
    path('jugadoresformulario', views.jugadoresformulario, name='formulariojugadores' ),
]
