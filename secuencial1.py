'''serie de Algoritmos realizados por Yurany Zuluaga Vargas G1 ACDI VOCA
Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto
dinero ganara después de un mes si el banco paga a razón de 2% mensual'''

print("Ejercicio 1")
cap_inv=float(input("Digite el capital a invertir"))
gan=cap_inv*0.02
print((gan))

#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el
#vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
#ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
#base y comisiones

print("Ejercicio 2")
sb=float(input("digite su salario basico"))
v1=float(input("digite su venta1"))
v2=float(input("digite su venta2"))
v3=float(input("digite su venta3"))
com=v1+v2+v3
tpag=sb+com
print("el total de pago es",tpag,"con unas comisiones de",com)

#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
#saber cuanto deberá pagar finalmente por su compra.

print("Ejercicio 2")
tc=float(input("digite el valor del total de la compra"))
d=tc*0.15
tp=tc-d
print("el total a pagar por su compra con el descuento es: ",tp)

#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha
#calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.
print("Ejercicio 3")
C1=float(input("digite su calificación 1"))
C2=float(input("digite su calificación 2"))
C3=float(input("digite su calificación 3"))
ef=float(input("digite la nota de su examen final"))
tf=float(input("digite la nota de su trabajo final"))
prom=(C1+C2+C3)/3
ppar=prom*55
pef=ef*0.30
ptf=tf*0.15
cf=ppar+pef+ptf
print("su calificación final es: ",cf)

#Un maestro desea saber que porcentaje de hombres y que porcentaje de mujeres hay en
#un grupo de estudiantes.
print("Ejercicio 4")
nm=float(input("digite el numero de mujeres"))
nh=float(input("digite el numero de hombres"))
ta=nh+nm
ph=nh*100/ta
pm=nm*100/ta
print("el porcentade de hombres es",ph, "el porcertaje de mujeres es",pm)

#Realizar un algoritmo que calcule la edad de una persona.
print("Ejercicio 5")
fnac=float(input("digite el año de su nacimiento"))
fact=float(input("digite el año actual"))
edad=fact-fnac
print(f"su edad es:{edad}")

print("Problemas propuestos")

#Dada un cantidad en pesos, obtener la equivalencia en dólares, asumiendo que la unidad
#cambiaría es un dato desconocido.
print("Ejercicio 1")
pesos=float(input("digite la cantidad en pesos"))
undolenpes=float(input("digite a cuanto equivale 1 dolar en pesos"))
conver=pesos*1/undolenpes
print("para el valor de un dolar en pesos de:",undolenpes,"la cantidad en pesos de",pesos, "equivale en dolares a",conver)

#Leer un numero y escribir el valor absoluto del mismo.
print("Ejercicio 2")
numeroej2=float(input("Ingrese el número al que quiere sacarle el valor absoluto"))
abso=print("el valor absoluto de",numeroej2," es", abs(numeroej2))

#La presión, el volumen y la temperatura de una masa de aire se relacionan por la formula:
#masa = (presión * volumen)/(0.37 * (temperatura + 460))
print("Ejercicio 3")
presion=float(input("ingrese la presion"))
volumen=float(input("digite el volumen"))
temperatura=float(input("digite la temperatura"))
masa = (presion*volumen)/(0.37 * (temperatura+460))
print("la masa es",masa)

#Calcular el numero de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la formula es:
#num. pulsaciones = (220 - edad)/10
print("Ejercicio 4")
edad=float(input("ingrese su edad"))
print("el numero de pulsasiones es: ",(220 - edad)/10)

#Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario anterior.
print("Ejercicio 5")
salant=float(input("ingrese su salario anterior"))
print("su nuevo salario con el incremento del 25% es: ",(salant+salant*0.25))

# En un hospital existen tres áreas: Ginecología, Pediatría, Traumatologia. El presupuesto anual del hospital
print("Ejercicio 6")
monpres=float(input("ingrese el monto presupuestal"))
print("el 40% para ginecologia es: ",monpres*0.4,"el 30% para traumatologia es:",monpres*0.3,"el 30% para pediatria es:",monpres*0.3)

#El dueño de una tienda compra un articulo a un precio determinado. Obtener el precio en que lo debe vender para obtener una ganancia del 30%.
print("Ejercicio 7")
preciocom=float(input("ingrese el precio de compra del artículo"))
print("con ganancia del 30% el costo al que debe venderlo es de ",(preciocom+preciocom*0.3))

#Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los
#tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer la
#ruta en una semana cualquiera.
print("Ejercicio 8")
tlunes=float(input("ingrese el tiempo cronometrado el lunes"))
tmiercoles=float(input("ingrese el tiempo cronometrado el miercoles"))
tviernes=float(input("ingrese el tiempo cronometrado el viernes"))
print("el tiempo promedio de la semana es de: ",(tlunes+tmiercoles+tviernes)/3)

#Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas
#invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con
#respecto a la cantidad total invertida.

print("Ejercicio 9")

totinv=float(input("ingrese el total invertido"))
inv1=float(input("ingrese la inversion 1 de la primera persona"))
inv2=float(input("ingrese la inversion 2 de la segunda persona"))
inv3=float(input("ingrese la inversion 3 de la tercera persona"))
print("el porcentaje de la inversion 1 es: ",(inv1*100)/totinv,"%")
print("el porcentaje de la inversion 2 es: ",(inv2*100)/totinv,"%")
print("el porcentaje de la inversion 3 es: ",(inv3*100)/totinv,"%")

#Un alumno desea saber cual será su promedio general en las tres materias mas difíciles
#que cursa y cual será el promedio que obtendrá en cada una de ellas. Estas materias se
#evalúan como se muestra a continuación:

print("Ejercicio 10")
print("Ingresar las notas con valores entre 0 y 5.0")
exmat=float(input("ingrese la nota del examen de matematicas del 90%"))
tar1mat=float(input("ingrese la nota de la tarea 1 de matematicas"))
tar2mat=float(input("ingrese la nota de la tarea 2 de matematicas"))
tar3mat=float(input("ingrese la nota de la tarea 3 de matematicas"))
promtarmat=(tar1mat+tar2mat+tar3mat)/3
prommat=(0.9*exmat+0.1*promtarmat)/100

xfis=float(input("ingrese la nota del examen de fisica del 80%"))
tar1fis=float(input("ingrese la nota de la tarea 1 de fisica"))
tar2fis=float(input("ingrese la nota de la tarea 2 de fisica"))
promtarfis=(tar1mat+tar2mat)/2
promfis=(0.8*exmat+0.2*promtarmat)/100

exmat=float(input("ingrese la nota del examen de matematicas del 85%"))
tar1quim=float(input("ingrese la nota de la tarea 1 de quimica"))
tar2quim=float(input("ingrese la nota de la tarea 2 de quimica"))
tar3quim=float(input("ingrese la nota de la tarea 3 de quimica"))
promtarquim=(tar1mat+tar2mat+tar3mat)/3
promquim=(0.9*exmat+0.1*promtarmat)/100

print("el promedio general de las 3 materias es: ",(prommat+promfis+promquim)/3)












