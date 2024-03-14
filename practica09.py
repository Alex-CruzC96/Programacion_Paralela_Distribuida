#NOMBRE PROGRAMADOR: Alejandro Cruz Cruz, Anael Gdp. Del Carpio Zenteno, Brithaly Jasmín Hernández Ramírez, Heber Jafet Álvaro Ramírez
#DESCRIPCION: Condiciones de Bairnstein
#FECHA: 13/03/2024
#HORA: 8:54

entradas1=[]
entradas2=[]
salidas1=[]
salidas2=[]
while(True):
    ent=input("Ingrese las entradas del proceso (deje vacio para terminar): ")
    if(ent==''):
        break
    else:
        entradas1.append(ent)

while(True):
    ent=input("Ingrese las salidas del proceso (deje vacio para terminar): ")
    if(ent==''):
        break
    else:
        salidas1.append(ent)

while(True):
    ent=input("Ingrese las entradas del proceso (deje vacio para terminar): ")
    if(ent==''):
        break
    else:
        entradas2.append(ent)

while(True):
    ent=input("Ingrese las salidas del proceso (deje vacio para terminar): ")
    if(ent==''):
        break
    else:
        salidas2.append(ent)


control=True

for i in entradas1:
    for j in salidas2:
        if(i==j):
            control=False

for i in salidas1:
    for j in entradas2:
        if(i==j):
            control=False

for i in salidas1:
    for j in salidas2:
        if(i==j):
            control=False


if(control):
    print("Sí es posible utilizar concurrencia")
else:
    print("No se puedo aplicar concurrencia")

    



