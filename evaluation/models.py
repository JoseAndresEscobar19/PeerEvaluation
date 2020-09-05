from django.db import models

# Create your models here.
class Group(models.Model):
    nombre=models.CharField(max_length=100)
    # num_estudiantes=models.IntegerField()
    def __str__(self):
        return self.nombre

class Student(models.Model):
    nombre=models.CharField(max_length=200)
    matricula=models.PositiveIntegerField()
    group=models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    paralelo=models.IntegerField(default=2)
    done=models.BooleanField(default=False)
    def __str__(self):
        return self.nombre+" "+str(self.group)

class Evaluacion(models.Model):
    estudiante=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    calificacion=models.PositiveIntegerField()