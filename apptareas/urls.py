from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('crear_tareas',views.crear_tareas,name='tareas'),
    path('editar_tareas',views.editar_tareas,name='editar'),
    
]