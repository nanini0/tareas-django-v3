from django import forms
from django.forms import ModelForm
from .models import *


class FormTarea(forms.ModelForm):

    class Meta:
        model = Tareas
        field = '__all__'