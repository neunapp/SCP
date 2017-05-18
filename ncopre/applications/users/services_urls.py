# django
from django.conf.urls import url

# local
from . import viewsets


urlpatterns = [
    #listar usuarios
    url(
        r'^api/userproceso/list/$',
        viewsets.ListUserViewSet.as_view({'get': 'list'}),
        name='api-procesoUsuario_list'
    ),
]
