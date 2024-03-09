

presupuesto1=2300
presupuesto2=700
total=680
medio=total/2
pago1=medio
pago2=medio

prom=(((pago1*100)/presupuesto1)+((pago2*100)/presupuesto2))/2
print(prom)


if presupuesto1 > presupuesto2:
    pago1=pago1+((prom*total)/100)
    pago2=pago2-((prom*total)/100)
    prom=(((pago1*100)/presupuesto1)+((pago2*100)/presupuesto2))/2
    print(prom)
    print(f"Pago 1 ha cambiado a = {pago1}\nPago 2 ha cambiado a = {pago2} \n ")
else:
    pago1=pago1-((prom*total)/100)
    pago2=pago2+((prom*total)/100)
    prom=(((pago1*100)/presupuesto1)+((pago2*100)/presupuesto2))/2
    print(f"Pago 1 ha cambiado a = {pago1}\nPago 2 ha cambiado a = {pago2} \n ")
