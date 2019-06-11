from django.contrib import admin

# Register your models here.
from .models import *

#,Beneficios,Competencias,Condiciones,Convenio,Departamento,Distrito,Escuela,Facultad,Horario,
# Institucion,Objetivos,Pais,Perfil,Perfil_Requerimiento,Plan_de_Capacitacion,Provincia,Representante,Requerimiento,Universidad
admin.site.register(Actividades)
admin.site.register(Autoridad)
admin.site.register(Beneficios)
admin.site.register(Competencias)
admin.site.register(Condiciones)
admin.site.register(Convenio)
admin.site.register(Departamento)
admin.site.register(Distrito)
admin.site.register(Escuela)
admin.site.register(Facultad)
admin.site.register(Horario)
admin.site.register(Institucion)
admin.site.register(Objetivos)
admin.site.register(Pais)
admin.site.register(Perfil)
admin.site.register(Perfil_Requerimiento)
admin.site.register(Plan_de_Capacitacion)
admin.site.register(Provincia)
admin.site.register(Representante)
admin.site.register(Requerimiento)
admin.site.register(Universidad)