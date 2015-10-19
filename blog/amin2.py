from django.contrib import admin
from .models import Nota
from inscripcions.models import Inscripcion

class NotaAdmin(admin.ModelAdmin):
	list_display = ('estudiante','fecha','calificacion','observacion')
	list_editable = ('estudiante','calificacion','observacion')
	List_filter = ('estudiante','fecha','calificacion','observacion')
	search_fields =('estudiante','fecha','calificacion','observacion')

admin.site.register(Nota, NotaAdmin)
