# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import *
# from image_cropping import ImageCropField,ImageRatioField
from django.db import models
# from geoposition.fields import GeopositionField
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Empleados(models.Model):
    id_empleados = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=150)
    cedula_empleado = models.CharField(max_length=350)

    class Meta:
    	verbose_name = 'Empleado'
    	verbose_name_plural = 'Empleados'
    	db_table = 'empleados'

    def __str__(self):
        return u'%s' %(self.nombre_empleado)

class TipoAusencias(models.Model):
    id_tipoausencias = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)

    class Meta:
    	verbose_name = 'Tipo Ausencia'
    	verbose_name_plural = 'Tipos de Ausencia'
    	db_table = 'tipoausencias'

    def __str__(self):
        return u'%s' %(self.id_tipoausencias)

class Permisos(models.Model):
    id_permisos = models.AutoField(primary_key=True)
    id_tipoausencias = models.ForeignKey(TipoAusencias, models.DO_NOTHING, db_column='id_tipoausencias', verbose_name='Tipo de Ausencia')
    id_empleados = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleados', verbose_name='Empleado')
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()

    class Meta:
    	verbose_name = 'Permiso'
    	verbose_name_plural = 'Permisos'
    	db_table = 'permisos'

    def __str__(self):
        return u'%s' %(self.id_permisos)