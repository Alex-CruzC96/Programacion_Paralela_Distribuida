#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz
#DESCRIPCION: Crear clase Reloj el cual dara la hora en el formato adecuado
#FECHA: 06/02/2024
#HORA: 17:38

class Tiempo1:
    def __init__(self, hora, minuto,segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def establecerTiempo(self, hora, minuto, segundo ):
        if (hora<0 or hora >=24 or minuto <0 or minuto >=60 or segundo <0 or segundo >=60):
            print("Error Hora invalida")
        else:
            self.hora = hora
            self.minuto = minuto
            self.segundo = segundo
    
    def aStringUniversal(self):
        return str(f"{self.hora:02.0f}:{self.minuto:02.0f}:{self.segundo:02.0f}")
    
    def toString(self):
        texto = 12 if (self.hora==0 or self.hora==12) else self.hora%12
        meridiano = "AM" if self.hora <12 else "PM"
        return str(f" {texto:02.0f}:{self.minuto:02.0f}:{self.segundo:02.0f} {meridiano}")

hora1 = Tiempo1(23,8,8)
print(hora1.toString())
print(hora1.aStringUniversal())