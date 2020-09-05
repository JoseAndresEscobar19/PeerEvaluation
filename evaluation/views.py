from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.db.models import Avg
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cargar_respuesta(request):
    if request.method == "POST":
        tmp=dict(request.POST)
        stu=tmp["stu_id"]
        cali=tmp["cali"]
        eva_id=tmp["eva_id"]
        evaluador=Student.objects.get(pk=eva_id[0])
        for stud,rate in zip(stu,cali):
            estudiante=Student.objects.get(pk=stud)
            try:
                eva=Evaluacion(estudiante=estudiante,calificacion=rate)
                eva.save()
            except:
                return render(request, 'index.html',{"msj":"Intenta de nuevo"})
        evaluador.done=True
        evaluador.save()
        return render(request, 'index.html',{"msj":"Gracias por enviar su evaluación"})
        
    else:
        grupos = Group.objects.order_by('nombre')
        estudiantes = Student.objects.order_by('nombre')
        matricula=request.GET.get("matricula",None)
        if matricula:
            try:
                matricula=int(matricula)
                stu=Student.objects.get(matricula=matricula)
                estudiantes = Student.objects.filter(paralelo=stu.paralelo,group_id=stu.group.pk).exclude(pk=stu.pk)
                if stu.done:
                    return render(request, 'index.html',{"msj":"Ya has realizado la evaluación"})
                else:
                    return render(request,"index.html",{"estudiantes":estudiantes,"est":stu})
            except:
                return render(request, 'index.html',{"msj":"Matrícula incorrecta"})
    
        return render(request, 'index.html',{"msj":"Matrícula incorrecta"})
        
def resumen_calificaciones_1(request):
    estudiantes=Student.objects.filter(paralelo=1).order_by('group').values_list('id', 'matricula')
    estudiantess=[]
    calificacion=[]
    promedio=[]
    for x,y in estudiantes:
        e = Student.objects.get(pk=x)
        calificacion_average = Student.objects.filter(pk=x).aggregate(avg=Avg('evaluacion__calificacion'))["avg"]
        if not calificacion_average:
            calificacion_average=0
        estudiantess.append(e)
        calificacion.append(calificacion_average)
        promedio.append(calificacion_average/5)
    return render(request,"estudiantes_list.html",{"resultado":zip(estudiantess,calificacion,promedio)})


def resumen_calificaciones_2(request):
    estudiantes=Student.objects.filter(paralelo=2).order_by('group').values_list('id', 'matricula')
    estudiantess=[]
    calificacion=[]
    promedio=[]
    for x,y in estudiantes:
        e = Student.objects.get(pk=x)
        calificacion_average = Student.objects.filter(pk=x).aggregate(avg=Avg('evaluacion__calificacion'))["avg"]
        if not calificacion_average:
            calificacion_average=0
        estudiantess.append(e)
        calificacion.append(calificacion_average)
        promedio.append(calificacion_average/5)
    return render(request,"estudiantes_list.html",{"resultado":zip(estudiantess,calificacion,promedio)})