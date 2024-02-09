#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz
#DESCRIPCION: Crea una clase llamada cuentaDeAhorros para calcular intereses mensuales
#FECHA: 09/02/2024
#HORA: 11:00

class cuentaDeAhorros:
    __tasaInteresAnual=None
    def __init__(self,saldoAhorros,tasaInteresAnual) -> None:
        self.__tasaInteresAnual=tasaInteresAnual
        self.saldoAhorros=saldoAhorros

    def calcularInteresMensual(self) -> float:
        self.saldoAhorros+=(self.saldoAhorros*((self.__tasaInteresAnual/12)/100))
        return self.saldoAhorros
    
    def modificarTasaInteres(self,tasaInteresAnual):
        self.tasaInteresAnual = tasaInteresAnual

ahorrador1=cuentaDeAhorros(2000,4)
ahorrador2=cuentaDeAhorros(3000,4)

print("Ahorrador 1 con 4% de tasa anual:")
for i in range(12):
    ahorro=ahorrador1.calcularInteresMensual()
    print(f"Mes {i+1} = "+"{:.2f}".format(ahorro))

print("\nAhorrador 2 con 4% de tasa anual:")
for i in range(12):
    ahorro=ahorrador2.calcularInteresMensual()
    print(f"Mes {i+1} = "+"{:.2f}".format(ahorro))

ahorrador1.modificarTasaInteres(5)
ahorrador2.modificarTasaInteres(5)

print("\nAhorrador 1 con 5% de tasa anual:")
for i in range(12):
    ahorro=ahorrador1.calcularInteresMensual()
    print(f"Mes {i+1} = "+"{:.2f}".format(ahorro))

print("\nAhorrador 2 con 5% de tasa anual:")
for i in range(12):
    ahorro=ahorrador2.calcularInteresMensual()
    print(f"Mes {i+1} = "+"{:.2f}".format(ahorro))
