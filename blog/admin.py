from django.contrib import admin
from .models  import Alumno, Aula, Carrera, Inscripcion, Institucion, Materia,Nota, Post, Seccion

class AlumnoAdmin(admin.ModelAdmin):
    list_display =  ('id','cedula','nombre','apellido','email')
    list_editable = ('id','cedula','nombre','apellido','email')
    List_filter =   ('id','cedula','nombre','apellido','email')
    search_fields = ('id','cedula','nombre','apellido','email')

class InscripcionAdmin(admin.ModelAdmin):
    list_display =  ('id','alumno','seccion','fecha')
    list_editable = ('id','alumno','seccion','fecha')
    List_filter =   ('id','alumno','seccion','fecha')
    search_fields = ('id','alumno','seccion','fecha')

class NotaAdmin(admin.ModelAdmin):
    list_display =  ('inscripcion','nota','fechaevalua','observacion')
    list_editable = ('inscripcion','nota','fechaevalua','observacion')
    List_filter =   ('inscripcion','nota','fechaevalua','observacion')
    search_fields = ('inscripcion','nota','fechaevalua','observacion')

class MateriaAdmin(admin.ModelAdmin):
    list_display =  ('id','carrera','nombre')
    list_editable = ('id','carrera','nombre')
    List_filter =   ('id','carrera','nombre')
    search_fields = ('id','carrera','nombre')

class PostAdmin(admin.ModelAdmin):
    list_display =  ('id','author','title','text')
    list_editable = ('id','author','title','text')
    List_filter =   ('id','author','title','text')
    search_fields = ('id','author','title','text')

class CarreraAdmin(admin.ModelAdmin):
    list_display =('id','institucion','nombre')

class AulaAdmin(admin.ModelAdmin):
    list_display =('id','direccion','nombre')

class SeccionAdmin(admin.ModelAdmin):
    list_display =('id','materia','aula','seccion')

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','sede','rif')

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Seccion, SeccionAdmin)
