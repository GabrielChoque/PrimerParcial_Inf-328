# INTERFAZ
import metodoFix
from tkinter import *
exp = ""
def pres(num):
	global exp
	exp = exp + str(num)
	ecuacion.set(exp)
def botonIgualpres():
    try:
        global exp
        respuesta = metodoFix.Infix(exp)
        ecuacion.set(metodoFix.setFormat1(respuesta))
        exp = metodoFix.setFormat2(respuesta)
    except:
        ecuacion.set("existe un error")
        exp = ""

def ac():
	global exp
	exp = ""
	ecuacion.set("")
def delete():
    global exp
    exp = exp[:-1]
    ecuacion.set(exp)

if __name__ == "__main__":
    ventana = Tk()
    ventana.configure(background="gray")
    ventana.title("calculadora")
    ventana.geometry("300x200")
    ecuacion = StringVar()
    expresion_campo = Entry(ventana, textvariable=ecuacion)
    expresion_campo.grid(columnspan=5, ipadx=70)
    
    boton7 = Button(ventana, text=' 7 ', fg='black', bg='green', command=lambda: pres(7), height=1, width=7)
    boton7.grid(row=2, column=0)
    boton8 = Button(ventana, text=' 8 ', fg='black', bg='red', command=lambda: pres(8), height=1, width=7)
    boton8.grid(row=2, column=1)
    boton9 = Button(ventana, text=' 9 ', fg='black', bg='blue', command=lambda: pres(9), height=1, width=7)
    boton9.grid(row=2, column=2)
    botonDel = Button(ventana, text='DEL', fg='black', bg='yellow', command=delete, height=1, width=7)
    botonDel.grid(row=2, column=3)
    botonAc = Button(ventana, text='AC', fg='black', bg='orange', command=ac, height=1, width=7)
    botonAc.grid(row=2, column=4)
    
    boton4 = Button(ventana, text=' 4 ', fg='black', bg='orange', command=lambda: pres(4), height=1, width=7)
    boton4.grid(row=3, column=0)
    boton5 = Button(ventana, text=' 5 ', fg='black', bg='yellow', command=lambda: pres(5), height=1, width=7)
    boton5.grid(row=3, column=1)
    boton6 = Button(ventana, text=' 6 ', fg='black', bg='blue', command=lambda: pres(6), height=1, width=7)
    boton6.grid(row=3, column=2)
    botonMultiplicar = Button(ventana, text=' * ', fg='black', bg='red', command=lambda: pres("*"), height=1, width=7)
    botonMultiplicar.grid(row=3, column=3)
    botonDividir = Button(ventana, text=' / ', fg='black', bg='green', command=lambda: pres("/"), height=1, width=7)
    botonDividir.grid(row=3, column=4)
    
    boton1 = Button(ventana, text=' 1 ', fg='black', bg='green', command=lambda: pres(1), height=1, width=7)
    boton1.grid(row=4, column=0)
    boton2 = Button(ventana, text=' 2 ', fg='black', bg='red', command=lambda: pres(2), height=1, width=7)
    boton2.grid(row=4, column=1)
    boton3 = Button(ventana, text=' 3 ', fg='black', bg='blue', command=lambda: pres(3), height=1, width=7)
    boton3.grid(row=4, column=2)
    botonSumar = Button(ventana, text=' + ', fg='black', bg='yellow', command=lambda: pres("+"), height=1, width=7)
    botonSumar.grid(row=4, column=3)
    botonRestar = Button(ventana, text=' - ', fg='black', bg='orange', command=lambda: pres("-"), height=1, width=7)
    botonRestar.grid(row=4, column=4)
    
    boton0 = Button(ventana, text=' 0 ', fg='black', bg='orange', command=lambda: pres(0), height=1, width=7)
    boton0.grid(row=5, column=0)
    botonPunto= Button(ventana, text='.', fg='black', bg='yellow', command=lambda: pres('.'), height=1, width=7)
    botonPunto.grid(row=5, column=1)
    botonIgual = Button(ventana, text=' = ', fg='black', bg='blue', command=botonIgualpres, height=1, width=7)
    botonIgual.grid(row=5, column=2)
    botonAbrirParentesis = Button(ventana, text=' ( ', fg='black', bg='red', command=lambda: pres("("), height=1, width=7)
    botonAbrirParentesis.grid(row=5, column=3)
    botonCerrarParentesis = Button(ventana, text=' ) ', fg='black', bg='green', command=lambda: pres(")"), height=1, width=7)
    botonCerrarParentesis.grid(row=5, column=4)
    
    ventana.mainloop()