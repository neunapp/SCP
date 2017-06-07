from django.db import models
<<<<<<< HEAD
from django.db.models import F, FloatField, Sum, Q, CharField
from django.db.models.functions import Upper
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    TrigramSimilarity
)


class BussinesUnitManager(models.Manager):
    """procedimiento que filtra eliminados de unidad de negocio"""

    def by_bussines(self):
        return self.filter(
            anulate=False,
        )



class ProcessManager(models.Manager):
    """Procedimiento para listar procesos por unidad de negocio"""

    def process_by_bussiness(self):
        # ---- argupa procesos por unidad de negocio ---
        #recuperaos la unidades de negocio factibles
        filtro_default = self.filter(
            anulate=False,
            close=False,
        )
        bussines = filtro_default.distinct(
            'bussinesunit__pk'
        ).values(
            'bussinesunit__pk','bussinesunit__razon_social',
        )

        #para cada unidad de negocio recuperamos sus procesos
        resultado = []
        #
        for b in bussines:
            procesos = filtro_default.filter(
                bussinesunit__pk=b['bussinesunit__pk'],
            ).order_by('-started')
            #cremos un diccionario
            dic_resultado = {
                'unida_negocio':b['bussinesunit__razon_social'],
                'procesos':procesos,
            }
            resultado.append(dic_resultado)
        #devolvemos resultado
        return resultado

    #
    def process_bunit(self, pk):
        return self.filter(
            anulate=False,
            bussinesunit=pk,
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


    #procedimiento para listar procesos recientes
    def proceso_todos(self):
        return self.filter(
            anulate=False,
            finished=True,
        ).order_by("-date_end")[:50]


    #funcion para filtrar proceso por nombre
    def process_search(self, kwords):
        #trasformamos kword
        kword = ''
        for k in kwords.split('-'):
            kword = kword + ' '+k

        return self.filter(
            anulate=False,
            started=True,
            name__trigram_similar=kword,
        ).order_by('-date_end')

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
<<<<<<< HEAD


    #proceso para cambiar boleano
    def validator_check(self, bool):
        if bool:
            return False
        else:
            return True



=======
>>>>>>> origin/master
