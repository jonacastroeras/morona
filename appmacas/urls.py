from django.conf.urls import *

from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from . import views
# from . import pdf


urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^listar_permisos$', views.listar_permisos, name='listar_permisos'),
	url(r'^nuevo_empleado$', views.nuevo_empleado, name='nuevo_empleado'),
	url(r'^listar_empleado$', views.listar_empleado, name='listar_empleado'),
	url(r'^modificar_empleado/(?P<ide>\d+)$', views.modificar_empleado, name='modificar_empleado'),

	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)