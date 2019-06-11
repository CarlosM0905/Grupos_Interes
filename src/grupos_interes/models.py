from django.db import models

# Create your models here.


class Universidad(models.Model):
    id_universidad = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=30)

class Facultad(models.Model):
    id_facultad = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=30)
    id_universidad = models.ForeignKey('Universidad', on_delete = models.CASCADE)

class Autoridad(models.Model):
    id_autoridad = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    grado = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=30)
    id_facultad = models.ForeignKey('Facultad', on_delete = models.CASCADE)

class Convenio(models.Model):
    id_convenio = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_escuela = models.ForeignKey('Escuela',on_delete=models.CASCADE)

class Plan_de_Capacitacion(models.Model):
    id_capacitacion = models.IntegerField(primary_key=True)
    id_convenio = models.ForeignKey('Convenio', on_delete = models.CASCADE)

class Actividades(models.Model):
    id_actividades = models.IntegerField(primary_key=True)
    funcion_principal = models.CharField(max_length=50)
    tareas_desprendidas = models.CharField(max_length=100)
    id_capacitacion = models.ForeignKey('Plan_de_Capacitacion', on_delete=models.CASCADE)

class Beneficios(models.Model):
    id_beneficio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    beneficiado = models.CharField(max_length=30)
    id_convenio = models.ForeignKey('Convenio',on_delete=models.CASCADE)

class Competencias(models.Model):
    id_competencias = models.IntegerField(primary_key=True)
    competencias_especificas = models.CharField(max_length=100)
    competencias_genericas = models.CharField(max_length=100)
    id_capacitacion = models.ForeignKey('Plan_de_Capacitacion',on_delete=models.CASCADE)

class Condiciones(models.Model):
    id_condiciones = models.IntegerField(primary_key=True)
    monto_de_la_subvencion = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_de_seguro_y_cobertura = models.CharField(max_length=20)
    ocupacion_o_puesto_de_trabajo = models.CharField(max_length=30)
    id_convenio = models.ForeignKey('Convenio', on_delete=models.CASCADE)

class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

class Departamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    id_pais = models.ForeignKey('Pais', on_delete = models.CASCADE)

class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    id_departamento = models.ForeignKey('Departamento', on_delete = models.CASCADE)


class Distrito(models.Model):
    id_distrito = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    id_provincia = models.ForeignKey('Provincia',on_delete= models.CASCADE)

class Escuela(models.Model):
    id_escuela = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    id_facultad = models.ForeignKey('Facultad', on_delete=models.CASCADE)

class Horario(models.Model):
    id_horario = models.IntegerField(primary_key=True)
    dias_trabajar = models.CharField(max_length=30)
    minimo_horas = models.IntegerField()
    maximo_horas = models.IntegerField()
    hora_salida = models.TimeField()
    hora_entrada = models.TimeField()
    id_condiciones = models.ForeignKey('Condiciones',on_delete=models.CASCADE)

class Institucion(models.Model):
    id_institucion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    pagina_web = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    ruc = models.IntegerField()
    id_distrito = models.ForeignKey('Distrito', on_delete = models.CASCADE)

class Objetivos(models.Model):
    id_objetivos = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    id_capacitacon = models.ForeignKey('Plan_de_Capacitacion',on_delete=models.CASCADE)

class Perfil(models.Model):
    id_perfil = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    id_institucion = models.ForeignKey('Institucion',on_delete=models.CASCADE)

class Requerimiento(models.Model):
    id_requerimiento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    area = models.CharField(max_length=30)

class Perfil_Requerimiento(models.Model):
    id_perfil_req = models.IntegerField(primary_key=True)
    prioridad = models.CharField(max_length=30)
    id_requerimiento = models.ForeignKey('Requerimiento',on_delete = models.CASCADE)
    id_perfil = models.ForeignKey('Perfil',on_delete=models.CASCADE)

class Representante(models.Model):
    id_representante = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    dni = models.CharField(max_length=11)
    id_institucion = models.ForeignKey('Institucion',on_delete=models.CASCADE)

