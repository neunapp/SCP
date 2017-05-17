from django.db import models
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class BussinesUnitManager(models.Manager):
    """procedimiento que filtra eliminados de unidad de negocio"""

    def by_bussines(self):
        return self.filter(
            anulate=False,
        )



class ProcessManager(models.Manager):
    """Procedimiento para listar procesos por unidad de negocio"""

    def process_bunit(self, pk):
        return self.filter(
            anulate = False,
            bussinesunit = pk,
        )

    #procedimiento que lita procesos que estan en proceso
    def proceso_filtro(self, pk, flat):
        if flat == '1':
        # filtra los precesos que estan en proceso
          return self.filter(
              bussinesunit=pk,
              anulate=False,
              finished=False
          )
        elif flat == '2':
        # filtrar Terminados
          return self.filter(
              bussinesunit=pk,
              finished=True
          )
        elif flat == '3':
        # filtrar eliminados
          return self.filter(
              bussinesunit=pk,
              anulate=True
          )
        else:
          print "consulta mal Hecha"


    #procedimiento para listar procesos recientes segun pk
    def proceso_todos(self, pk):
        return self.filter(
            bussinesunit=pk,
            anulate=False,
            finished=False
        ).order_by("-pk")


    #prueba trigram postgresql
    def proceso_pruebanombre(self, pk, namep):
        return self.annotate(
           search=SearchVector('name')
        ).filter(
            search=namep,
            bussinesunit=pk,
            anulate=False,
            finished=False
        ).order_by('-pk')[0:50]





