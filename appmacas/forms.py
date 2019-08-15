from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,TextInput,FileInput,NumberInput,DateInput,Select,CheckboxSelectMultiple,Textarea,ModelMultipleChoiceField
from django.utils.safestring import mark_safe
from django import forms
from django.utils.translation import gettext as _
from appmacas.models import *


class  Empleado_Form(ModelForm):
	class Meta:
		model = Empleados
		fields = '__all__'

class  Permisos_Form(ModelForm):
	class Meta:
		model = Permisos
		fields = '__all__'
		widgets = {
			'fecha_desde': DateInput(attrs={'class':'form-control', 'type': 'date'}),
			'fecha_hasta': DateInput(attrs={'class':'form-control', 'type': 'date'}),
		}
		# labels={
		# 		'art_nombre_artistico': u'Nombre Artístico *',
		# 		'art_logo': 'Suba su logo',
		# 		'art_imagen': 'Suba una foto *',
		# 		'art_nombre_real': 'Nombre Real *',
		# 		'art_cedula': u'Cédula *',
		# 		'art_acercade': u'Acerca de Mí (una breve descripción) *',
		# 		'art_fecha_nac': 'Fecha de Nacimiento *',
		# 		'id_nacionalidad': u'País de Origen *',		
		# 		'art_ocupacion': u'Ocupación *',
		# 		'art_estilo': 'Estilo *',
		# 		'art_premios': 'Premios',
		# 		'institucion': u'Institución *',
		# 		'art_fecha_inicio': 'Fecha Inicio Actividades *',
		# 		'art_registro': u'Registro Artístico Sayce',
		# 		'productora': 'Productora',
		# 		'sello_discografico': u'Sello discográfico',
		# 		'art_url': u'URL (Página Web)',
		# 		'art_spotify': 'Spotify',
		# 		'art_facebook': 'Facebook',
		# 		'art_twitter': 'Twitter',
		# 		'art_instagram': 'Instagram',
		# 		'art_soundcloud': 'Souncloud',
		# 		'art_youtube': 'Youtube',
		# 		'art_audio': 'URL, video de Youtube propio del Artista',
		# 		'art_dir': u'Dirección (domicilio) *',
		# 		'art_telefono_fijo': u'Teléfono Fijo',
		# 		'art_celular': 'Celular *',
		# 		'art_mail': 'E-mail *',
		# 		'art_man_nombre': 'Nombre',
		# 		'art_man_direccion': u'Dirección',
		# 		'art_man_telefono_fijo': 'Telefono Fijo',
		# 		'art_man_cel': 'Celular',
		# 		'art_man_mail': 'E-mail',
		# 		'art_man_web': 'Web',
		# 		'art_respaldo_certificaciones': 'Respaldo certificaciones',
		# 		'art_respaldo_portafolio':'Respaldo Portafolio (URL)',
		# 		'id_estudio_musical': 'Estudio Musical:',
		# 		'art_ciudad_origen': 'Ciudad Origen: *',
		# 		'art_ciudad_residencia': 'Ciudad Residencia: *',				
		# 		'id': 'Id',


		# }