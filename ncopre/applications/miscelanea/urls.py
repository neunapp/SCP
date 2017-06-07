from django.conf.urls import url, include

# local
from . import views


urlpatterns = [
    url(
        r'^procesoobservacion/listar/(?P<pk>\d+)/$',
        views.ProcessDetailMisceleaView.as_view(),
        name='Proceso_list_miscelanea'
    ),

    url(
        r'^procesoservicio/agregar/(?P<pk>\d+)/$',
        views.ServiceProcessView.as_view(),
        name='Proceso_list_miscelanea'
    ),







    # rest de Miscelanea
    url(r'^', include('applications.miscelanea.services_urls', namespace="Miscelanea_servis_url")),
]