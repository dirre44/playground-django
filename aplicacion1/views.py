from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.

def crear_curso (request):

    nombre_curso = "sonido"
    comision_curso = "2434"
    curso = Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta = f"curso creado: {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)

def listar_cursos(request):
    cursos = Curso.objects.all()
    respuesta = ""
    for curso in cursos:
        respuesta += f"{curso.nombre} - {curso.comision}<br>"
    return HttpResponse(respuesta)

def inicio(request):
    return render(request,"inicio.html")

def profesores(request):
    return render(request,"profesores.html")

def cursos(request):
    cursos = Curso.objects.all()
    return render(request,"cursos.html", {"cursos":cursos})

def estudiantes(request):
    return render(request,"estudiantes.html")

def entregables(request):
    return render(request,"entregables.html")