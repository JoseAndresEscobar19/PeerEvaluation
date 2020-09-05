from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subir-eva/', views.cargar_respuesta, name='cargar_datos'),
    path('ver-calificaciones-par-1/', views.resumen_calificaciones_1, name='resumen_calificaciones_1'),
    path('ver-calificaciones-par-2/', views.resumen_calificaciones_2, name='resumen_calificaciones_2'),
]