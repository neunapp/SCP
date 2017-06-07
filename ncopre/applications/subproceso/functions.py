#applicacion item
from applications.item.models import DetailProcess, Item
#applicacion subproceso
from .models import FieldsSubProcess


#clase que representa un Campo de SubProceso
class Field_Subprocess():
    field = None
    items = None


#clase que representa un SubProceso
class Sub_Process():
    sub_proceso = None
    fields = []


#funcion que devuleve actividades de un proceso
def get_activitys_process(pk_proceso):
    #lista resultado
    resultado = []
    #recuperamos sub procesos de un proceso por pk
    subprocess = DetailProcess.objects.filter(
        process__pk=pk_proceso,
    ).order_by('-created')
    #para cada sub process recuperamos Field
    for sp in subprocess:
        #creamos objeto sub prcoeso
        s_p = Sub_Process()
        s_p.sub_proceso = sp
        s_p.fields = []
        #recuperamos sub procesos
        fields_subprocess = FieldsSubProcess.objects.filter(
            sub_process=sp.sub_process,
        )
        #para cada Fiedl Recupero items
        for fs in fields_subprocess:
            #creamos objeto FieldsSubProcess
            f_s = Field_Subprocess()
            f_s.field = fs
            f_s.items = Item.objects.filter(
                detail_camp_subprocess=fs,
            ).order_by('created')
            #agregamos a sub proceso
            s_p.fields.append(f_s)
        #agregamos a reultado
        resultado.append(s_p)
    #devolvemos el resultado
    return resultado
