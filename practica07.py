from datetime import date
from datetime import datetime

class perfilMedico:
    def __init__(self,nombre1,apellido,dia,mes,año,altura,peso,genero):
        self.nombre1 = nombre1
        self.apellido = apellido
        self.dia =  dia
        self.mes = mes
        self.año = año
        self.altura=altura
        self.peso=peso
        self.genero=genero

    def establecernombre(self,nombre1):
        self.nombre1 = nombre1
    def devolvernombre(self):
        return self.nombre1

    def establecerapellido(self,apellido):
        self.apellido=apellido
    def devolverapellido(self):
        return self.apellido
    
    def establecerdia(self,dia):
        self.dia= dia
    def devolverdia(self):
        return self.dia
    
    def establecermes(self,mes):
        self.mes=mes
    def devolvermes(self):
        return self.mes
    
    def estableceraño(self,año):
        self.año=año
    def devolveraño(self):
        return self.año
    
    def estableceraltura(self,altura):
        self.altura = altura
    def devolveraltura(self):
        return self.altura
    
    def establecerpeso(self,peso):
        self.peso = peso
    def devolverpeso(self):
        return self.peso
    
    def establecergenero(self,genero):
        self.genero=genero
    def devolvergenero(self):
        return self.genero
    
    def calcularedad(self): #
        hoy= 2024
        edad = hoy - self.devolveraño()
        return edad
        
    

    def fcmaxima(self):
        edad= self.calcularedad()
        return 220-edad
    def fcesperada(self):
        valor=[]
        inferior= self.fcmaxima() *0.5
        superior= self.fcmaxima () * 0.85
        #0print("inferior: ", inferior,"superior: ", superior)
        valor.append(inferior)
        valor.append(superior)
        return valor

    def BMI (self):
        masa = self.devolverpeso()/ self.devolveraltura() ** 2
        if masa < 18.5 :
            print("bajo peso")
        elif masa > 18.5 and masa <= 24.9:
            print("peso normal")
        elif masa >= 25 and masa <= 29.9:
            print("sobre peso ")
        else:
            print("obeso")
        return masa



paciente = perfilMedico("brith","hernandez",8,2,2004,1.50,55,"femenino")
print("Nombre: ",paciente.devolvernombre())
print("Apellido: ",paciente.devolverapellido())
print("Altura: ",paciente.devolveraltura())
print("Peso: ",paciente.devolverpeso())
print("Genero: ",paciente.devolvergenero())
print("Frecuencia maxima: " , paciente.fcmaxima())
print("Frecuencia esperada: " , paciente.fcesperada())
print("Indice de masa corporal: " , paciente.BMI())
print("Edad calculada: " , paciente.calcularedad())
      
        