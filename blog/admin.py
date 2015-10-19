from django.contrib import admin
from .models  import Alumno, Aula, Carrera, Inscripcion, Institucion, Materia,Nota, Post, Seccion


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido')
    list_editable = ('nombre','apellido')
    List_filter = ('nombre','apellido')
    search_fields =('nombre','apellido')

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('alumno','seccion','fecha')
    list_editable = ('alumno','seccion','fecha')
    List_filter = ('alumno','seccion','fecha')
    search_fields =('alumno','seccion','fecha')

class NotaAdmin(admin.ModelAdmin):
    list_display = ('inscripcion','nota','fechaevalua')
    list_editable = ('inscripcion','nota','fechaevalua')
    List_filter = ('inscripcion','nota','fechaevalua')
    # search_fields =('alumno','seccion')

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('carrera','nombre')
    list_editable = ('carrera','nombre')
    List_filter = ('carrera','nombre')
    search_fields =('carrera','nombre')

class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','text')
    #list_editable = ('carrera','nombre')
    #List_filter = ('carrera','nombre')
    #search_fields =('carrera','nombre')

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Aula)
admin.site.register(Carrera)
admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(Institucion)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Seccion)
