from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subir-eva/', views.cargar_respuesta, name='cargar_datos'),
    path('ver-calificaciones/', views.resumen_calificaciones, name='resumen_calificaciones'),
]