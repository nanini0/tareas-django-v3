from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('editar_tareas/<int:pk>/', views.editar_tareas, name='editar'),
    
]