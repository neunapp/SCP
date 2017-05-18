from __future__ import absolute_import

from rest_framework import serializers

# import local
from .models import User


class ListUserSerializer(serializers.ModelSerializer):
    """Serializador para listar Usuarios para procesos"""

    class Meta:
        model = User
        fields = (
            'pk',
            'username'
        )
