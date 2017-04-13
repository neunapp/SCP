from __future__ import unicode_literals

from django.db import models

#third party
from model_utils.models import TimeStampedModel
# Create your models here.

#django
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class SubProcess(TimeStampedModel):
    """Django data model Subprocess"""

    name = models.TextField('nombre', max_length=100)
    description = models.TextField('descripcion', max_length=700)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Field(TimeStampedModel):
    """Django data model campos"""

    TYPE_INT = 'I'
    TYPE_STRING = 'S'
    TYPE_CHOICES = (
        (TYPE_INT, 'entero'),
        (TYPE_STRING, 'cadena'),
    )
    name = models.TextField('nombre', max_length=70)
    type = models.CharField(
        'tipo',
        max_length=6,
        choices = TYPE_CHOICES
    )
    required = models.BooleanField(default=True)
    description = models.TextField('descripcion')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class FieldsSubProcess(TimeStampedModel):
    """django data model campossubprocesos"""

    sub_process = models.ForeignKey('SubProcess')
    field = models.ForeignKey('Field')

    def __str__(self):
        return self.sub_process




