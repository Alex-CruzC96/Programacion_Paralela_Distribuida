
class Problema:
    fecha=None
    sucursal_Procedencia=None
    tipo_Problema=None
    def __init__(self,fecha,sucursal_Procedencia,tipo_Problema) -> None:
        self.fecha=fecha
        self.sucursal_Procedencia=sucursal_Procedencia
        self.tipo_Problema=tipo_Problema

class Reporte:
    problema=None
    departamento=None
    num_Reporte=None
    fecha_Creacion=None
    fecha_Fin=None
    def __init__(self,problema,departamento,num_reporte,fecha_Creacion) -> None:
        self.problema=problema
        self.departamento=departamento
        self.num_Reporte=num_reporte
        self.fecha_Creacion=fecha_Creacion

class Departamento:
    dep_Id=None
    nom_Dep=None
    responsable=None
    def __init__(self,dep_Id,nom_Dep,responsable) -> None:
        self.dep_Id=dep_Id
        self.nom_Dep=nom_Dep
        self.responsable=responsable

class Procesos:
    def evaluarProb(self,problema,depa,fecha_creacion):
        if(problema.tipo_Problema == "Tecnico"):
            reporte=Reporte(problema,depa,1,"21-02-2024") 
            return reporte
        elif (problema.tipo_Problema == "Legal"):
            pass
        elif (problema.tipo_Problema == "RH"):
            pass
        elif (problema.tipo_Problema == "Economico"):
            pass

    def evaluarNumRep(self):
        pass

depa1=Departamento(1,"Sistemas","Juanito")
problema1=Problema("21-02-2024","sucursal-1","Tecnico")
categorias=["Tecnico","Legal","RH","Economico"]
proceso=Procesos()
repo=proceso.evaluarProb(problema1,depa1,"21-02-2024")
print(repo.problema.tipo_Problema)
# if(problema1.tipo_Problema=="Tecnico"):
#     reporte=Reporte(problema1,depa1,1,"21-02-2024")

# #print(reporte.problema.tipo_Problema)
# print(reporte.departamento.nom_Dep)
# reporte.fecha_Fin="22-02-2024"
# print(reporte.fecha_Fin)