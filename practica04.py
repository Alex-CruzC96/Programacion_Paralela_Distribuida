#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz
#DESCRIPCION: Crear clase PolizaAuto para representar la poliza de un automovil 
#FECHA: 01/02/2024
#HORA: 19:55

class PolizaAuto:
    def __init__(self,numeroCuenta,marcaYModelo,estado) -> None:
        self._numeroCuenta=numeroCuenta
        self._marcaYModelo=marcaYModelo
        self._estado=estado

    def establecerNumeroCuenta(self,numeroCuenta):
        self._numeroCuenta=numeroCuenta
    
    def obtenerNumeroCuenta(self) -> int:
        return self._numeroCuenta
    
    def establecerMarcaYModelo(self,marcaYModelo):
        self._marcaYModelo=marcaYModelo
    
    def obtenerMarcaYModelo(self) -> str:
        return self._marcaYModelo
    
    def establecerEstado(self,estado):
        self._estado=estado

    def obtenerEstado(self) -> str:
        return self._estado
    
    def esEstadoSinCulpa(self) -> bool:
        estadoSinCulpa=None
        if(self.obtenerEstado() == "MA" or self.obtenerEstado() == "NJ" or self.obtenerEstado() == "NY" or self.obtenerEstado() == "PA"):
            estadoSinCulpa = True
        else:
            estadoSinCulpa = False
        return estadoSinCulpa
    

poliza1=PolizaAuto(11111111,"Toyota Camry","NJ")
poliza2=PolizaAuto(22222222,"Ford Fusion","ME")


