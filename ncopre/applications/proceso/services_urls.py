# django
from django.conf.urls import url

# local
from . import viewsets


urlpatterns = [
    #Unidad de negocio
    url(r'^api/unidadnegocio/nuevo/$',
        viewsets.BussinesUnitAddViewSet.as_view({'post': 'create'}),
        name='api_unidadnegocio-add'
    ),


    url(r'^api/unidadnegocio/list/$',
        viewsets.BussinesUnitListViewSet.as_view({'get': 'list'}),
        name='api_unidadnegocio-list'
    ),


    url(

        r'^api/unidadnegocio/retrieve/(?P<pk>[-\w]+)/$',
        viewsets.BussinesUnitRetriveViewSet.as_view({'get': 'retrieve'}),
        name='api-unidadnegocio_retrive'
    ),


    url(
        r'^api/unidadnegocio/update/$',
        viewsets.BussinesUnitUpdateViewSet.as_view({'post': 'create'}),
        name='api-unidadnegocio_update'
    ),


    url(
        r'^api/unidadnegocio/estado/$',
        viewsets.BussinesUnitUpdateStateAnulateViewSet.as_view({'post': 'create'}),
        name='api-unidadnegocioestado_update'
    ),

    #agregar Proceso
    url(
        r'^api/proceso/nuevo/$',
        viewsets.ProcessAddViewSet.as_view({'post': 'create'}),
        name='api-process_add'
    ),

    #listar proceso por unidad de negcio
    url(r'^api/proceso/list/(?P<pk>[-\w]+)/$',
        viewsets.ProcessListForBussinesUnitViewSet.as_view({'get': 'list'}),
        name='api_process_bunit-list'
    ),


    #listar usuarios
    url(
        r'^api/userproceso/list/$',
        viewsets.ListUserViewSet.as_view({'get': 'list'}),
        name='api-procesoUsuario_list'
    ),

    # listar
    url(
        r'^api/filtroproceso/listar/(?P<pk>[-\w]+)/(?P<flat>[-\w]+)/$',
        viewsets.ProcesoUnidadNegocioFilterEnprocesoViewSet.as_view({'get': 'list'}),
        name='api-procesofiltro_list'
    ),


]