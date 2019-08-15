# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class EmpleadosAdmin(admin.ModelAdmin):

    list_display = ('id_empleados', 'nombre_empleado', 'cedula_empleado')


class TipoAusenciasAdmin(admin.ModelAdmin):

    list_display = ('id_tipoausencias', 'nombre')


class PermisosAdmin(admin.ModelAdmin):

    list_display = (
        'id_permisos',
        'id_tipoausencias',
        'id_empleados',
        'fecha_desde',
        'fecha_hasta',
    )
    list_filter = (
        'id_tipoausencias',
        'id_empleados',
        'fecha_desde',
        'fecha_hasta',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Empleados, EmpleadosAdmin)
_register(models.TipoAusencias, TipoAusenciasAdmin)
_register(models.Permisos, PermisosAdmin)
