from funconecta4 import contador
import sys
tablero = [[" " for j in range(7)] for i in range(6)]
juego = True
contadorX = 0
contadorO = 0


def imprimirTablero():
    print("    1 2 3 4 5 6 7")
    for i in range(len(tablero)):
        x = "|".join(tablero[i])

        y = i + 1
        print(y, " |" + x + "|")
    print("-" * 24)

def colocarFichas():
    col = input("Introduce una columna: ")
    try:
        col = int(col)
        col -= 1
    except ValueError as ex:
        print(f"{ex!r}", file=sys.stderr)
    fil = 5
    while True:
        if col not in range(0, len(tablero) + 1) or tablero[0][col] != " ":
            if col not in range(0, len(tablero) + 1):
                col = input("Esta columna no es valida, intenta con otra: ")
            elif tablero[0][col] != " ":
                col = input("Esta columna esta llena, intenta con otra: ")
            try:
                col = int(col)
                col -= 1
            except ValueError as ex:
                print(f"{ex!r}", file=sys.stderr)
 
        else:
            for m in range(0, len(tablero)):
                if tablero[fil - m][col] == " ":
                    tablero[fil - m][col] = turno
                    return fil-m, col

turno = "X"
print("Parten las X")
while juego:
    imprimirTablero()
    (i, j) = colocarFichas()
    if turno == "X":
        contadorX = contador(tablero, "X", i, j)
        if contadorX >= 4:
            imprimirTablero()
            print("Las 'X' ganan!")
            juego = False
        else:
            turno = "O"
    elif turno == "O":
        contadorO = contador(tablero, "O", i, j)
        if contadorO >= 4:
            imprimirTablero()
            print("Los 'O' ganan!")
            juego = False
        else:
            turno = "X"
