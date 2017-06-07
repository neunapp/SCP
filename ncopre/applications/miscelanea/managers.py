from django.db import models



class MiscelaneaManager(models.Manager):
    """procedimiento que lista observaciones segun tipo"""

    def observacion_tipo(self, pk):
       return self.filter(
            process=pk,
            anulate=False,
        ).order_by('type_observation').order_by('description')