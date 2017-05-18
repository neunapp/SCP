from __future__ import absolute_import

from rest_framework import serializers

#loca import

from applications.item.models import Item


class ItemAddSerializer(serializers.ModelSerializer):
    """Serializador para sub Item"""

    field_key = serializers.CharField()

    class Meta:
        model = Item
        fields = (
            'value',
            'field_key',
        )
