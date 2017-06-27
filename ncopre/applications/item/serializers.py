from __future__ import absolute_import

from rest_framework import serializers

#loca import

from applications.item.models import Item, DetailProcess


class DetailProcessSerializer(serializers.ModelSerializer):
    """Serializador generico para DetailProcess"""
    name = serializers.CharField(source='sub_process.name')
    description = serializers.CharField(source='sub_process.description')
    pk = serializers.CharField()

    class Meta:
        model = DetailProcess
        fields = (
            'process',
            'sub_process',
            'name',
            'description',
            'pk',
        )


class ItemSerializer(serializers.ModelSerializer):
    """Serializador generico para item"""

    pk = serializers.CharField()

    class Meta:
        model = Item
        fields = (
            'detail_process',
            'detail_camp_subprocess',
            'tipy_item',
            'value',
            'pk',
        )


class ItemAddSerializer(serializers.ModelSerializer):
    """Serializador para sub Item"""

    field_key = serializers.CharField()

    class Meta:
        model = Item
        fields = (
            'value',
            'field_key',
        )

