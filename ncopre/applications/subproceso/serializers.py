from __future__ import absolute_import

from rest_framework import serializers

#import item
from applications.item.serializers import ItemAddSerializer
#loca import
from applications.subproceso.models import (
    SubProcess,
    FieldsSubProcess,
    Field,
)


class SubProcessSerializer(serializers.ModelSerializer):
    """Serializador para sub Proceso"""

    pk_proceso = serializers.CharField()

    class Meta:
        model = SubProcess
        fields = (
            'name',
            'description',
            'pk_proceso',
        )


class FieldSerializer(serializers.ModelSerializer):
    """Serializador para Modelo Campo"""

    class Meta:
        model = Field
        fields = (
            'name',
            'type_field',
            'required',
        )


class SubProcessAddSerializer(serializers.Serializer):
    """ serializador para agregar un nuevo proceso """
    sub_process = SubProcessSerializer()
    fields = FieldSerializer(many=True)
    items = ItemAddSerializer(many=True)
