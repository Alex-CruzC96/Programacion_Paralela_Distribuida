#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz
#DESCRIPCION: Crear clase estudiante
#FECHA: 01/02/2024
#HORA: 19:40

class Estudiante:
    def __init__(self,nombre,promedio) -> None:
        self._nombre=nombre
        if(promedio > 0.0 and promedio <= 100):
            self._promedio=promedio

    def establecerNombre(self,nombre) -> None:
        self._nombre=nombre
    
    def obtenerNombre(self) -> str:
        return self._nombre
    
    def establecerPromedio(self,promedio):
        if(promedio > 0.0 and promedio <= 100):
            self._promedio=promedio

    def obtenerPromedio(self) -> float:
        return self._promedio
    
    def obtenerCalificacionEstudiante(self) -> str:
        calificacionEstudiante = ''
        if self._promedio >= 90.0:
            calificacionEstudiante = 'A'
        elif self._promedio >= 80:
            calificacionEstudiante = 'B'
        elif self._promedio >= 70:
            calificacionEstudiante = 'C'
        elif self._promedio >= 60:
            calificacionEstudiante = 'D'
        else:
            calificacionEstudiante = "D"
        return calificacionEstudiante
    

estudiante1 = Estudiante("Jane Green",93.5)
estudiante2 = Estudiante("Jhon Blue",72.75)
print(f"La calificacion en letra de {estudiante1.obtenerNombre()} es {estudiante1.obtenerCalificacionEstudiante()}")
print(f"La calificacion en letra de {estudiante2.obtenerNombre()} es {estudiante2.obtenerCalificacionEstudiante()}")