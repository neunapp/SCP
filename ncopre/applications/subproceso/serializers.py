from __future__ import absolute_import

from rest_framework import serializers

#import item
from applications.item.serializers import (
    ItemAddSerializer,
    ItemSerializer,
    DetailProcessSerializer,
)
#loca import
from applications.subproceso.models import (
    SubProcess,
    FieldsSubProcess,
    Field,
)


class SubProcessSerializer(serializers.ModelSerializer):
    """Serializador para sub Proceso"""

    pk_proceso = serializers.CharField(required=False)

    class Meta:
        model = SubProcess
        fields = (
            'name',
            'description',
            'pk_proceso',
        )


class FieldSerializer(serializers.ModelSerializer):
    """Serializador para Modelo Campo"""
    sub_process = serializers.CharField(required=False)

    class Meta:
        model = Field
        fields = (
            'name',
            'type_field',
            'required',
            'sub_process',
        )


class FieldsSubProcessSerializer(serializers.ModelSerializer):
    """Serializador para Modelo Campo"""
    name = serializers.CharField(source='field.name')
    type_field = serializers.CharField(source='field.type_field')
    required = serializers.CharField(source='field.required')

    class Meta:
        model = FieldsSubProcess
        fields = (
            'name',
            'type_field',
            'required',
            'sub_process',
            'field',
        )


class FieldSubprocessSerializer(serializers.Serializer):
    """serializador para campos de un sub proceso"""
    field = FieldsSubProcessSerializer()
    items = ItemSerializer(many=True)


class GetProcessActivitySerializer(serializers.Serializer):
    """ serializador para recuperar actividades de un proceso """
    sub_proceso = DetailProcessSerializer()
    fields = FieldSubprocessSerializer(many=True)
