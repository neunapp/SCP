from django.conf.urls import url, include

# local
from . import views
urlpatterns = [

    url(
        r'^unidadnegocio/agregar/$',
        views.BussinesUnitAddView.as_view(),
        #primero aplicacion, nombrebasededatos-accion
        name='proceso-unidadnegocio_add'
    ),

    url(r'^unidadnegocio/update/(?P<pk>\d+)/$',
        views.BussinesUnitUpdateView.as_view(),
        name='proceso-unidadnegocio_update'
    ),

    # url lista BussinesUnit
    url(
        r'^unidadnegocio/listar/$',
        views.BussinesUnitLitView.as_view(),
        name='proceso-unidadnegocio_list'
    ),

    url(r'^proceso/add/(?P<pk>\d+)/$',
        views.ProcessAddView.as_view(),
        name='proceso-process_add'
        ),

    #url lista procesos por unidad de negocio
    url(
        r'^procesounidadnegocio/list/(?P<pk>\d+)/$',
        views.ProceessForBunitView.as_view(),
        name='proceso-por-unidadnegocio_list'
    ),

    #url lista procesos recientes
    url(
        r'^procesounidadnegocioreciente/listar/(?P<pk>\d+)/$',
        views.ProcessNowBunitView.as_view(),
        name='proceso-reciente-unidadnegocio_list'
    ),

    #rest de Unidad de negocio
    url(r'^', include('applications.proceso.services_urls', namespace="UnidadNegocio_servis_url")),
]