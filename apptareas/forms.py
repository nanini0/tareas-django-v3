from django.forms import ModelForm

from django import forms
from .models import Tareas

class FormTarea(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['nombre', 'descripcion','completado'] 