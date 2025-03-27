from django.shortcuts import render,redirect
from .models import * 
from .forms import *

# Create your views here.

def inicio(request):
    tareas = Tareas.objects.all()
    form = FormTarea()

    if request.method == 'POST':
        form = FormTarea(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'tareas': tareas, 'form': form}

    return render(request, 'inicio.html', context)


def editar_tareas(request,pk):
    tarea = Tareas.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method=="POST":
        form = FormTarea(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'editar_tareas.html',context)



