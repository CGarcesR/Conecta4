from funconecta4 import contador
import tkinter as tk

class Turno:
    turno = "X"

ventana = tk.Tk()
tablero = [["   " for j in range(7)] for i in range(6)]
t = Turno()

def salir():
    ventana.destroy()

def actualizar():
    for i in range(len(tablero)):
        fila = tk.Label(ventana, text=("   |   ".join(tablero[i])))
        filas = tk.Label(ventana, text=(i + 1))
        fila.grid(row=i + 1, column=1, padx=5, pady=5, columnspan=7)
        filas.grid(row=i + 1, column=0, padx=5, pady=5)

    turno_ventana = tk.Label(ventana, text=("Turno = " + t.turno))
    turno_ventana.grid(row=7, column=5, padx=5, pady=5, columnspan=5)


def colocarFichas(columna):
    col = columna
    fil = 5
    if tablero[0][col] != "   ":
        print("Esta columna esta llena, intenta con otra: ")
    else:
        for m in range(0, len(tablero)):
            if tablero[fil - m][col] == "   ":
                tablero[fil - m][col] = t.turno
                contadorX = contador(tablero, t.turno, fil - m, col)
                if contadorX >= 4:
                    mensaje = tk.Label(ventana, text=("Las", t.turno, "ganan!"))
                    mensaje.grid(row=8, column=2, padx=5, pady=5, columnspan=5)
                    boton_salir = tk.Button(ventana, text="Terminar Juego", command = salir)
                    boton_salir.grid(row=9, column=4, padx=5, pady=5, columnspan=5)
                    boton1 = tk.Button(ventana, text="1")
                    boton2 = tk.Button(ventana, text="2")
                    boton3 = tk.Button(ventana, text="3")
                    boton4 = tk.Button(ventana, text="4")
                    boton5 = tk.Button(ventana, text="5")
                    boton6 = tk.Button(ventana, text="6")
                    boton7 = tk.Button(ventana, text="7")
                    boton1.grid(row=0, column=1, padx=4, pady=5)
                    boton2.grid(row=0, column=2, padx=4, pady=5)
                    boton3.grid(row=0, column=3, padx=4, pady=5)
                    boton4.grid(row=0, column=4, padx=4, pady=5)
                    boton5.grid(row=0, column=5, padx=4, pady=5)
                    boton6.grid(row=0, column=6, padx=4, pady=5)
                    boton7.grid(row=0, column=7, padx=4, pady=5)
                    actualizar()
                t.turno = "X" if t.turno == "O" else "O"
                actualizar()
                break
