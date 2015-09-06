from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lista_entradas, name='lista_entradas'),
    url(r'^entrada/(?P<pk>[0-9]+)/$', views.detalle_entrada, name='detalle_entrada'),
    url(r'^entrada/nueva/$', views.nueva_entrada, name='nueva_entrada'),
    url(r'^entrada/(?P<pk>[0-9]+)/editar/$', views.editar_entrada, name='editar_entrada'),
]