#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz
#DESCRIPCION: Primer programa, practica acerca de las clases en python
#FECHA: 01/02/2024
#HORA: 10:31

class Perro:
    especie='mamifero'
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza

    def ladra(self):
        print("Guau!")
    
    def caminar(self,pasos):
        print(f"He caminado {pasos} pasos")
        
    def dormir(self):
        print("...")


perro=Perro('Bachicha','Salchicha')
perro.ladra()
perro.caminar(10)
perro.dormir()