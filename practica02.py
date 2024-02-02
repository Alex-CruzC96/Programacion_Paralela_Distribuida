#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz
#DESCRIPCION: Crear clase para el uso de un banco
#FECHA: 01/02/2024
#HORA: 19:24

class Cuenta:
    def __init__(self,nombre,saldo) -> None:
        self._nombre=nombre
        if (saldo > 0.0):
            self._saldo=saldo
    
    def depositar(self,montoDeposito) -> None:
        if(montoDeposito > 0.0):
            self._saldo+=montoDeposito

    def obtenerSaldo(self) -> float:
        return self._saldo
    
    def establecerNombre(self,nombre):
        self._nombre=nombre

    def obtenerNombre(self) -> str:
        return self._nombre
    
miCuenta=Cuenta('Alejandro',10)
