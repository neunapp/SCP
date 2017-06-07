# django
from django.conf.urls import url

# local
from . import viewsets


urlpatterns = [
    # Lista Observaciones
    url(r'^api/observacion/listar/(?P<pk>[-\w]+)/$',
        viewsets.ObservationListViewSet.as_view({'get': 'list'}),
        name='api_observation-list'
    ),


    # actualiza setado de observation
    url(r'^api/observacion/update/$',
        viewsets.ObservationStateUpdateViewSet.as_view({'post': 'create'}),
        name='api_observation-updatestate-list'
    ),


    #agrega observacion
    url(r'^api/observacion/add/$',
        viewsets.ObservationAddViewSet.as_view({'post': 'create'}),
        name='api_observation-add-list'
    ),

    #agreaga servicio y actualiza proceso
    url(r'^api/servicio/add/$',
        viewsets.ServiceAddThirdViewSet.as_view({'post': 'create'}),
        name='api_servicio-add-list'
    ),

]