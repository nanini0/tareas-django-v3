from django.shortcuts import render
from .models import * 

# Create your views here.

def inicio(request):
    tareas = Tareas.objects.all()
    return render(request,'inicio.html',{'tareas':tareas})

def crear_tareas(request):
    return render(request,'crear_tareas.html')

def editar_tareas(request):
    return render(request,'editar_tareas.html')



