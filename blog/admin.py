from django.contrib import admin
from .models  import Alumno, Aula, Carrera, Inscripcion, Institucion, Materia,Nota, Post, Seccion

class AlumnoAdmin(admin.ModelAdmin):
    list_display =  ('cedula','nombre','apellido')
    list_editable = ('cedula','nombre','apellido')
    List_filter =   ('cedula','nombre','apellido')
    search_fields = ('cedula','nombre','apellido')

class InscripcionAdmin(admin.ModelAdmin):
    list_display =  ('alumno','seccion','fecha')
    list_editable = ('alumno','seccion','fecha')
    List_filter =   ('alumno','seccion','fecha')
    search_fields = ('alumno','seccion','fecha')

class NotaAdmin(admin.ModelAdmin):
    list_display =  ('inscripcion','nota','fechaevalua','observacion')
    list_editable = ('inscripcion','nota','fechaevalua','observacion')
    List_filter =   ('inscripcion','nota','fechaevalua','observacion')
    search_fields = ('inscripcion','nota','fechaevalua','observacion')

class MateriaAdmin(admin.ModelAdmin):
    list_display =  ('carrera','nombre')
    list_editable = ('carrera','nombre')
    List_filter =   ('carrera','nombre')
    search_fields = ('carrera','nombre')

class PostAdmin(admin.ModelAdmin):
    list_display =  ('author','title','text')
    list_editable = ('author','title','text')
    List_filter =   ('author','title','text')
    search_fields = ('author','title','text')

admin.site.register(Alumno)
admin.site.register(Aula)
admin.site.register(Carrera)
admin.site.register(Inscripcion)
admin.site.register(Institucion)
admin.site.register(Materia)
admin.site.register(Nota)
admin.site.register(Post, PostAdmin)
admin.site.register(Seccion)
