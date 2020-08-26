'''Ejericio nota de estudiantes, realizado por Yurany Zuluaga Vargas cc 1017210847 ACDI VOCA G1'''

from tkinter import *

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Nota de curse Algoritmos")
ventana.resizable(False, False)
titulo = Label(ventana, text="Calcula la nota final", font=('Arial', 14, 'bold'), height=3)
titulo.grid(row=0, column=1)

#agreguemos las notas

nota_1 = Label(ventana, text="Nota 1")
nota_1.grid(row=1, column=0)

nota_2 = Label(ventana, text="Nota 2")
nota_2.grid(row=2, column=0)

nota_3 = Label(ventana, text="Nota 3")
nota_3.grid(row=3, column=0)

nota_1_entry = Entry(ventana, width="8")
nota_1_entry.grid(row=1, column=1)

nota_2_entry = Entry(ventana, width="8")
nota_2_entry.grid(row=2, column=1)

nota_3_entry = Entry(ventana, width="8")
nota_3_entry.grid(row=3, column=1)

#agreguemos el promedio

promedio = Label(ventana)
promedio.grid(row=4, column=0)

nota_prom = Label(ventana)
nota_prom.grid(row=4, column=1)

#agreguemos el examen

nota_examen = Label(ventana, text="Exámen Final")
nota_examen.grid(row=5, column=0)
examen_entry = Entry(ventana, width="8")
examen_entry.grid(row=5, column=1)

#agreguemos el trabajo

nota_trabajo = Label(ventana, text="Trabajo Final")
nota_trabajo.grid(row=6, column=0)
trabajo_entry = Entry(ventana, width="8")
trabajo_entry.grid(row=6, column=1)

#empleamos el botón calcular
#la instruccion dos puntos, punto efe, me permite reducir el numero de decimales

def calcularNota():
    nota1 = float(nota_1_entry.get())
    nota2 = float(nota_2_entry.get())
    nota3 = float(nota_3_entry.get())
    promedio_alumno = (nota1 + nota2 + nota3) / 3
    examen_alumno = float(examen_entry.get())
    trabajo_alumno = float(trabajo_entry.get())
    nota_final = promedio_alumno * 0.55 + examen_alumno * 0.3 + trabajo_alumno * 0.15

    promedio['text'] = 'Promedio'
    nota_prom['text'] = f'{promedio_alumno:.2f}'
    notaFinal['text'] = 'Nota Final'
    final['text'] = f'{nota_final:.2f}'


notaFinal = Label(ventana)
notaFinal.grid(row=7, column=0)
final = Label(ventana)
final.grid(row=7, column=1)

calcular = Button(ventana, text="Calcular", command=calcularNota)
calcular.place(x=0, y=250)

ventana.mainloop()