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
    sede    = models.CharField(max_length=18,default='CC Chaguaramos')
    rif     = models.CharField(max_length=18)
    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    institucion = models.ForeignKey(Institucion)
    nombre = models.CharField(max_length=35,default='Tecnico Superior en Informatica')
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    carrera = models.ForeignKey(Carrera)
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return self.nombre

class Aula(models.Model):
    nombre = models.CharField(max_length=8)
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Seccion(models.Model):
    materia = models.ForeignKey(Materia)
    aula = models.ForeignKey(Aula)
    seccion = models.CharField(max_length=10)
    def __str__(self):
        return self.seccion

class Alumno(models.Model):
    cedula   = models.IntegerField(unique=True)
    nombre   = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email    = models.EmailField(default='a@a.com')
    def __str__(self):
        nalumno = self.nombre+self.apellido
        return nalumno

class Inscripcion(models.Model):
    alumno  = models.ForeignKey(Alumno)
    seccion = models.ForeignKey(Seccion)
    fecha =   models.DateTimeField(blank=True, null=True)
    def inscrito(self):
        self.fecha= timezone.now()
        self.save()
    def __str__(self):
        return self.alumno

class Nota(models.Model):
    inscripcion = models.ForeignKey(Inscripcion)
    fechaevalua = models.DateTimeField(default=timezone.now)
    nota        = models.IntegerField(default=0)
    observacion = models.CharField(max_length=50,default='no asistio')
    def __str__(self):
        return self.inscripcion
