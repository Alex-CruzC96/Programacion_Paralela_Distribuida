#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz y Anael G. Del Carpio Zenteno
#DESCRIPCION: Interfaces formales
#FECHA: 29/02/2024
#HORA: 8:32

from abc import ABC
from abc import ABCMeta
from abc import abstractmethod

class Mando( metaclass = ABCMeta):
    @abstractmethod
    def siguiente_canal(self):
        pass

    @abstractmethod
    def canal_anterior(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass

class MandoSamsung (Mando):
    def siguiente_canal(self):
        print("Samsung -> siguiente")
    def canal_anterior(self):
        print("Samsung -> anterior")
    def subir_volumen(self):
        print("Samsung -> subir")
    def bajar_volumen(self):
        print("Samsung -> bajar")

mando_samsung = MandoSamsung()
mando_samsung.bajar_volumen()            