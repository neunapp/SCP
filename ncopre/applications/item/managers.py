from django.db import models
from django.db.models import CharField
from django.db.models.functions import Upper,Lower, Cast


class DetailProcessManager(models.Manager):
    """procedimientos para detalle proceso"""

    def get_process_activitys(self,pk):
        return self.filter(
            process__pk=pk,
        ).annotate(
            name=Upper('sub_process__name'),
            pk_proceso=Cast('sub_process__id',CharField(max_length=10)),
            description=Lower('sub_process__description'),
        )
