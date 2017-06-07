from django.db import models
from django.db.models import CharField
from django.db.models.functions import Upper,Lower,Cast


class FieldsSubProcessManager(models.Manager):
    """procedimientos para FieldsSubProcess"""

    def get_subprocess_fields(self,pk):
        return self.filter(
            sub_process__pk=pk,
        ).annotate(
            name=Upper('field__name'),
            type_field=Lower('field__type_field'),
            required=Cast('field__required',CharField(max_length=5)),
            description=Lower('field__description'),
        )
