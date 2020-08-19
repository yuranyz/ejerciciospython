""" Problemas resueltos por Yurany Zuluaga Vargas G1 ACDI VOCA
Un hombre desea saber cuanto dinero se genera por concepto de intereses sobre la
cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses siempre y
cuando estos excedan a $7000, y en ese caso desea saber cuanto dinero tendrá finalmente
en su cuenta."""

p_int=float(input("ingrese el p_int"))
cap=float(input("ingrese el capital"))
inte=cap*p_int
if inte>7000:
    capf=cap+inte
    print("el capital final es",capf)
    print("puede invertir")
else:
    print("mejor no invertir")

#Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.
calif1=float(input("ingrese la calificación 1"))
calif2=float(input("ingrese la calificación 2"))
calif3=float(input("ingrese la calificación 3"))
prom=(calif1+calif2+calif3)/3
if prom>=70:
    print("alumno aprobado")
else:
    print("alumno reprobado")

#En un almacén se hace un 20% de descuento a los clientes cuya compra supere los $1000
#¿ Cual será la cantidad que pagara una persona por su compra?
compra=float(input("digite el valor de su compra"))
if compra>1000:
    desc=compra*0.20
else:
    desc=0
tot_pag=compra-desc
print(f"\n si tiene descuento y debe pagar:{tot_pag}")

#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:Si trabaja 40 horas o menos se le paga $16 por hora
#Si trabaja mas de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
ht=float(input("ingrese las horas de trabajo"))
if ht>40:
    he=ht-40
    ss=he*20+40*16
else:
    ss=ht*16
print(f"\n su salario semanal es:{ss}")

#Que lea dos números y los imprima en forma ascendente
num1=float(input("ingrese el numero 1"))
num2=float(input("ingrese el numero 2"))
if num1<num2:
    print("los números de forma ascendente",num1,num2)
else:
    print("los números de forma ascendente", num2, num1)


