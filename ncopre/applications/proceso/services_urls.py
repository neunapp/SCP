# django
from django.conf.urls import url

# local
from . import viewsets


urlpatterns = [
    #agregar Unidad de negocio
    url(r'^api/unidadnegocio/nuevo/$',
        viewsets.BussinesUnitAddViewSet.as_view({'post': 'create'}),
        name='api_unidadnegocio-add'
    ),

    # Lista unidad de negocio
    url(r'^api/unidadnegocio/list/$',
        viewsets.BussinesUnitListViewSet.as_view({'get': 'list'}),
        name='api_unidadnegocio-list'
    ),

    #recuperar unidad de negocio
    url(
        r'^api/unidadnegocio/retrieve/(?P<pk>[-\w]+)/$',
        viewsets.BussinesUnitRetriveViewSet.as_view({'get': 'retrieve'}),
        name='api-unidadnegocio_retrive'
    ),

    #ctualizar unidad de negocio
    url(
        r'^api/unidadnegocio/update/$',
        viewsets.BussinesUnitUpdateViewSet.as_view({'post': 'create'}),
        name='api-unidadnegocio_update'
    ),

    #anular unidad de negocio
    url(
        r'^api/unidadnegocio/estado/$',
        viewsets.BussinesUnitUpdateStateAnulateViewSet.as_view({'post': 'create'}),
        name='api-unidadnegocioestado_update'
    ),

    # Lista procesos agrupados por unidad de negocio
    url(r'^api/proceso/por-unidad-negocio/$',
        viewsets.ProcessByBusiness.as_view({'get': 'list'}),
        name='api_proceso-list_unidad_negocio'
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

    # listar proceso por unidad de negocio
    url(
        r'^api/filtroproceso/listar/(?P<pk>[-\w]+)/(?P<flat>[-\w]+)/$',
        viewsets.ProcesoUnidadNegocioFilterEnprocesoViewSet.as_view({'get': 'list'}),
        name='api-procesofiltro_list'
    ),

    # recuperar proceso por nombre
    url(
        r'^api/proceso/retrieve/(?P<pk>[-\w]+)/$',
        viewsets.ProcessGetViewSet.as_view({'get': 'retrieve'}),
        name='api-proceso_retrive'
    ),

    # buscar procesos por nombre
    url(
      r'^api/proceso/buscar/(?P<kword>[-\w]+)/$',
        viewsets.ProcesoSearchViewSet.as_view({'get':'list'}),
        name='api-proceso_search'
    ),


    #listar procesos recientes
    url(
        r'^api/procesoreciente/listar/$',
        viewsets.ProcessRecentViewSet.as_view({'get': 'list'}),
        name='api-procesoreciente_list'
    ),


    #guardar estados proceso
    url(
        r'^api/procesoestado/cambiar/$',
        viewsets.ProcessStateChangeViewSet.as_view({'post': 'create'}),
        name='api-procesoestado_update'
    ),
]
