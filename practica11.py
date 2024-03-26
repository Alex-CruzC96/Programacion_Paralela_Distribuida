#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz, Anael Gdp. Del Carpio Zenteno, Brithaly Jasmín Hernández Ramírez, Heber Jafet Álvaro Ramírez
#DESCRIPCION: Contador par e impar
#FECHA: 22/03/2024
#HORA: 8:37

import threading

def pares():
    print([i for i in range(100) if i % 2 ==0])

def impares():
    print([i for i in range(100) if i % 2 != 0])

hilo1=threading.Thread(target=impares)
hilo2=threading.Thread(target=pares)

hilo1.start()
hilo1.join()
hilo2.start()
