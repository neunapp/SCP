# django
from django.conf.urls import url

# local
from . import viewsets


urlpatterns = [
    #agregar Unidad de negocio
    url(r'^api/sub-proceso/add/$',
        viewsets.SubProcessAddViewSet.as_view({'post': 'create'}),
        name='api_sub_process-add'
    ),
]
