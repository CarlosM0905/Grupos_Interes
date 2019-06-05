from django.db import models

# Create your models here.

class Plan_de_capacitacion(models.Model):
    id_capacitacion = models.IntegerField()

class Universidad(models.Model):
    id_universidad = models.IntegerField()
    nombre = models.CharField(max_length=30)


class Actividades(models.Model):
    id_actividades = models.IntegerField()
    funcion_principal = models.CharField(max_length=50)
    tareas_desprendidas = models.CharField(max_length=100)
    id_capacitacion = models.ForeignKey(Plan_de_capacitacion, on_delete=models.CASCADE)

class Facultad(models.Model):
    id_facultad = models.IntegerField()
    nombre = models.CharField(max_length=30)
    id_universidad = models.ForeignKey(Universidad,on_delete=models.CASCADE) 

class Autoridad(models.Model):
    id_autoridad = models.IntegerField()
    nombre = models.CharField(max_length = 30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    grado = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=30)
    id_facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    


    
class Convenio(models.Model):
    id_convenio = models.IntegerField()
    tipo = models.CharField(max_length = 30)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
class Pais(models.Model):
    id_pais = models.IntegerField()
    nombre = models.CharField(max_length=30)

class Departamento(models.Model):
    id_departamento = models.IntegerField()
    nombre = models.CharField(max_length=30)
    id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE)

class Escuela(models.Model):
    id_escuela = models.IntegerField()
    nombre = models.CharField(max_length = 30)
    id_facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
class Provincia(models.Model):
    id_provincia = models.IntegerField()
    nombre = models.CharField(max_length=30)
    id_departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)

class Distrito(models.Model):
    id_distrito = models.IntegerField()
    nombre = models.CharField(max_length=30)
    id_provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE)

class Institucion(models.Model):
    id_institucion = models.IntegerField()
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    pagina_web = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ruc = models.IntegerField()
    id_distrito = models.ForeignKey(Distrito,on_delete=models.CASCADE)









"""class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
"""