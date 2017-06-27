# django
from django.conf.urls import url

# local
from . import viewsets


urlpatterns = [
    #recupera actividades de proceso
    url(r'^api/get-process-activity/(?P<pk>[-\w]+)/$',
        viewsets.GetProcessActivitys.as_view({'get': 'list'}),
        name='api_get_activity_process-list'
    ),
    #recupera Fields de un subproceso
    url(r'^api/get-subprocess-fields/(?P<pk>[-\w]+)/$',
        viewsets.GetSubProcessFields.as_view({'get': 'list'}),
        name='api_get_subprocess_fields-list'
    ),
    #agregar Actividad de Proceso
    url(r'^api/activity-proceso/add/$',
        viewsets.ActivityProcessAddViewSet.as_view({'post': 'create'}),
        name='api_activity_process-add'
    ),
    #agregar Field de SubProceso - add campo de sub proceso
    url(r'^api/field-subprocess/add/$',
        viewsets.FieldAddViewSet.as_view({'post': 'create'}),
        name='api_field_subprocess-add'
    ),

    #actualizar field de vaoucher
    url(r'^api/field-voucher/return/(?P<pk>[-\w]+)/$',
        viewsets.GetVoucherFieldViewSet.as_view({'get': 'list'}),
        name='api_field_voucher-list'
    ),

    # guardar field de vaoucher
    url(r'^api/field-voucher/add/$',
        viewsets.SaveVoucherFieldViewset.as_view({'post': 'create'}),
        name='api_field_voucher-add'
    ),

    #cantidad de facturas por processo
    # guardar field de vaoucher
    url(r'^api/field-voucher/count/(?P<pk>[-\w]+)/$',
        viewsets.GetVoucherSetViewSet.as_view({'get': 'list'}),
        name='api_field_voucher-count'
    ),

]
