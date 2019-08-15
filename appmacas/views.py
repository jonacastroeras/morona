from django.shortcuts import render
from django.shortcuts import render, redirect
# from .forms import *
from .models import *
from datetime import datetime
from django.http import JsonResponse
import pytz, datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from appmacas.forms import *
from crispy_forms.helper import FormHelper

def index(request):

	# formulario = Permisos()
	if request.method == 'POST' and 'btn_guardar' in request.POST:
		formulario = Permisos_Form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect('/listar_permisos')
	else:
		formulario = Permisos_Form()
	ctx = {'formulario':formulario}
	# texto = ("Hello world")
	# if request.method == "POST" and "ingresar" in request.POST:
	# 	usuario = request.POST['usuario']
	# 	password = request.POST['password']
	# 	user = authenticate(username=usuario, password=password)
	# 	if user is not None:
	# 	# if request.user.is_authenticated():
	# 		if user.is_active:
	# 			login(request, user)
	# 			if user.is_superuser:
	# 				return redirect('lista_alumnos')
	# 			else:
	# 				# ide = Empresas.objects.get(propietario_id = user.id).pk
	# 				return redirect('')
	return render(request, 'index.html', ctx)

def listar_permisos(request):
	permisos = Permisos.objects.all()
	contador = 0
	nombre_columna = []
	diccionario = []
	for c in permisos:
		if c.id_tipoausencias.nombre in nombre_columna:
			pass
		else:
			nombre_columna.append(c.id_tipoausencias.nombre)
			for d in permisos:
				if c.id_tipoausencias.nombre == d.id_tipoausencias.nombre:
					contador = contador + 1
			diccionario.append({'empleado': c.id_empleados.nombre_empleado,'nombre_columna': c.id_tipoausencias.nombre, 'contador':contador, 'id_tipoausencias':str(c.id_tipoausencias)})
		contador = 0
	
	ctx = {'permisos' : permisos, 'diccionario':diccionario}
	return render(request, 'listar_permisos.html', ctx)

def nuevo_empleado(request):

	# formulario = Permisos()
	if request.method == 'POST' and 'btn_guardar' in request.POST:
		# emp = Empleados(request.POST,request.FILES,instance=instance)
		formulario = Empleado_Form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect('/listar_empleado')
	else:
		formulario = Empleado_Form()
		ctx = {'formulario':formulario}
		return render(request, 'nuevo_empleado.html', ctx)
	ctx = {}
	return render(request, 'nuevo_empleado.html', ctx)

def modificar_empleado(request, ide):

	# formulario = Permisos()
	instance = Empleados.objects.get(id_empleados = ide)
	if request.method == 'POST' and 'btn_guardar' in request.POST:
		# emp = Empleados(request.POST,request.FILES,instance=instance)
		formulario = Empleado_Form(request.POST, instance = instance)
		if formulario.is_valid():
			formulario.save()
			return redirect('/listar_empleado')
	else:
		formulario = Empleado_Form(instance = instance)
		ctx = {'formulario':formulario}
		return render(request, 'nuevo_empleado.html', ctx)
	ctx = {}
	return render(request, 'nuevo_empleado.html', ctx)


def listar_empleado(request):
	empleados = Empleados.objects.all()
	# formulario = Permisos()
	
	ctx = {'empleados':empleados}
	return render(request, 'listar_empleado.html', ctx)