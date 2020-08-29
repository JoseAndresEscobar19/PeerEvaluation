from django import forms
from .models import *
from django.forms.models import inlineformset_factory




class EvaluacionForm(forms.ModelForm):

    class Meta: 
        model= Evaluacion
        fields = "__all__"
        labels = {
            "calificacion":'',
            "estudiante":''
        }
        widgets={
            "calificacion":forms.NumberInput(attrs={"max":5,"min":0,"required":True}),
            "estudiante":forms.HiddenInput()
        }