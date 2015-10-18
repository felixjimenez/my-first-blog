from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date= timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Institucion(models.Model):
    nombre  = models.CharField(max_length=18,default='IUTIRLA')
    sede    = models.CharField(max_length=18,default='Chaguaramos')
    rif     = models.CharField(max_length=18)

class Carrera(models.Model):
    institucion = models.ForeignKey(Institucion)
    nombre = models.CharField(max_length=18,default='Informatica')

class Materia(models.Model):
    carrera = models.ForeignKey(Carrera)
    nombre = models.CharField(max_length=20)

class Aula(models.Model):
    nombre = models.CharField(max_length=8)
    direccion = models.CharField(max_length=15)

class Seccion(models.Model):
    materia = models.ForeignKey(Materia)
    aula = models.ForeignKey(Aula)
    seccion = models.CharField(max_length=10)

class Alumno(models.Model):
    cedula   = models.IntegerField()
    nombre   = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email    = models.EmailField()
#    foto     = models.ImageField()

class Inscripcion(models.Model):
    alumno  = models.ForeignKey(Alumno)
    seccion = models.ForeignKey(Seccion)
    fecha   = models.DateField(default=timezone)

class Nota(models.Model):
    inscripcion = models.ForeignKey(Inscripcion)
    fechaevalua = models.DateField(default=timezone)
    nota = models.IntegerField(default=0)
