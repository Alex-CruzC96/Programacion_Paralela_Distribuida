#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz, Anael Gdp. Del Carpio Zenteno
#DESCRIPCION: Calculo de suma de elementos en una lista de 100,000
#FECHA: 26/03/2024
#HORA: 11:49

import threading
import numpy as np

#almacena los resultados de las sumas de cada array
resultados=[]
#funcion que hace la suma de cada array dado
def suma(array):
    resultados.append(sum(array))

#array de elementos del 1 al 100000
elementos=np.array([i for i in range(1,100001)])

#numero de divisiones del array
n=20
#arrays divididos en 10 array de 5,000 elementos
arrays=np.array_split(elementos,n)

#array que almacena cada uno de los hilos que se ejecutan
hilos=[]
#los array estan dividios en 20 (i) cada uno con 5,000 elementos (arr)
for i,arr in  enumerate(arrays):
    hilo = threading.Thread(target=suma, args=(arr,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

total=sum(resultados)
print(f"La suma total de elementos es: {total}")
