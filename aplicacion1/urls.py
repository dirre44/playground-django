from django.urls import path, include
from .views import *

urlpatterns = [
    path("cursos/", cursos, name="cursos"),
    path("", inicio, name="inicio"),
    path("profesores/", profesores, name="profesores" ),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables")
]