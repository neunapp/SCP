#import django
from django.shortcuts import get_object_or_404

#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#appication proceso
from applications.proceso.models import Process
#aplication item
from applications.item.models import DetailProcess, Item
#impor local
from .serializers import (
    SubProcessAddSerializer,
    SubProcessSerializer,
    FieldSerializer,
)
#
from .models import (
    SubProcess,
    FieldsSubProcess,
    Field,
)

class SubProcessAddViewSet(viewsets.ViewSet):
    """viewset para agregar sub proceso a un proceso"""

    def create(self, request):
        serializado = SubProcessAddSerializer(data=request.data)
        if serializado.is_valid():
            #recuperamos proceso y registramos sub proceso
            proceso = Process.objects.get(
                pk=serializado.validated_data['sub_process']['pk_proceso'],
            )
            #
            sub_proceso = SubProcess(
                name=serializado.validated_data['sub_process']['name'],
                description=serializado.validated_data['sub_process']['description'],
            )
            sub_proceso.save()
            print 'sub Proceso guarado'
            print sub_proceso
            #registramos el detalle proceso relacion proceso sub proceso
            detalle_proceso = DetailProcess(
                process=proceso,
                sub_process=sub_proceso,
            )
            detalle_proceso.save()
            print 'detalle proceso guarado'
            #Regisramos los campos clave o fields
            detalle_campo_subprocesos = []
            for f in serializado.validated_data['fields']:
                field = Field(
                    name=f['name'],
                    type_field=f['type_field'],
                    required=f['required'],
                )
                field.save()
                'Field guarado'
                #registramos la relacion con el proceso
                field_sub_proceso = FieldsSubProcess(
                    sub_process=sub_proceso,
                    field=field,
                )
                field_sub_proceso.save()
                print 'Detalle Campos sub proceso guarado'
                #alamcen temporal de FieldsSubProcess para no consultar bd
                detalle_campo_subprocesos.append(field_sub_proceso)

            #registramos los item de cada Field
            for i in serializado.validated_data['items']:
                aux = 0
                #determinamos a que Field pertenece
                while aux >= 0:
                    if i['field_key'] != detalle_campo_subprocesos[aux].field.name:
                        aux = aux + 1
                    else:
                        aux = -1
                        item = Item(
                            detail_process=detalle_proceso,
                            detail_camp_subprocess=detalle_campo_subprocesos[aux],
                            value=i['value'],
                        )
                        item.save()

            print 'Sub Proceso guardado correctamente'
        else:
            print serializado.errors

        return Response()
