#import django
from django.shortcuts import get_object_or_404

#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#local import
from .serializers import ListUserSerializer
#
from .models import User


class ListUserViewSet(viewsets.ModelViewSet):
    """VIewset usuairo"""

    serializer_class = ListUserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
