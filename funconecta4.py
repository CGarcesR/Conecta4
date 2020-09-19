def contador(tablero, turno, i, j):
    con = 1
    if j-1 in range(len(tablero[i])) and tablero[i][j-1] == turno:
        con += 1
        if j-2 in range(len(tablero[i])) and tablero[i][j-2] == turno:
            con += 1
            if j-3 in range(len(tablero[i])) and tablero[i][j-3] == turno:
                con += 1
                return con
            elif j+1 in range(len(tablero[i])) and tablero[i][j+1] == turno:
                con += 1
                return con
            else:
                con = 1
        elif j+1 in range(len(tablero[i])) and tablero[i][j+1] == turno:
            con += 1
            if j+2 in range(len(tablero[i])) and tablero[i][j+2] == turno:
                con += 1
                return con
            else:
                con = 1
        else:
            con = 1
    elif j+1 in range(len(tablero[i])) and tablero[i][j+1] == turno:
        con += 1
        if j+2 in range(len(tablero[i])) and tablero[i][j+2] == turno:
            con += 1
            if j + 3 in range(len(tablero[i])) and tablero[i][j + 3] == turno:
                con += 1
                return con
            else:
                con = 1
        else:
            con = 1
    else:
        con = 1

    if i-1 in range(len(tablero)) and tablero[i-1][j] == turno:
        con += 1
        if i-2 in range(len(tablero)) and tablero[i-2][j] == turno:
            con += 1
            if i-3 in range(len(tablero)) and tablero[i-3][j] == turno:
                con += 1
                return con
            elif i+1 in range(len(tablero)) and tablero[i+1][j] == turno:
                con += 1
                return con
            else:
                con = 1
        elif i+1 in range(len(tablero)) and tablero[i+1][j] == turno:
            con += 1
            if i+2 in range(len(tablero)) and tablero[i+2][j] == turno:
                con += 1
                return con
            else:
                con = 1
        else:
            con = 1
    elif i+1 in range(len(tablero)) and tablero[i+1][j] == turno:
        con += 1
        if i+2 in range(len(tablero)) and tablero[i+2][j] == turno:
            con += 1
            if i + 3 in range(len(tablero)) and tablero[i+3][j] == turno:
                con += 1
                return con
            else:
                con = 1
        else:
            con = 1
    else:
        con = 1

    if i-1 in range(len(tablero)) and j-1 in range(len(tablero[i])) and tablero[i-1][j-1] == turno:
        con += 1
        if i-2 in range(len(tablero)) and j-2 in range(len(tablero[i])) and tablero[i-2][j-2] == turno:
            con += 1
            if i-3 in range(len(tablero)) and j-3 in range(len(tablero[i])) and tablero[i-3][j-3] == turno:
                con += 1
                return con
            elif i+1 in range(len(tablero)) and j+1 in range(len(tablero[i])) and tablero[i+1][j+1] == turno:
                con += 1
                return con
            else:
                con = 1
        elif i+1 in range(len(tablero)) and j+1 in range(len(tablero[i])) and tablero[i+1][j+1] == turno:
            con += 1
            if i+2 in range(len(tablero)) and j+2 in range(len(tablero[i])) and tablero[i+2][j+2] == turno:
                con += 1
                return con
            else:
                con = 1
        else:
            con = 1
    elif i+1 in range(len(tablero)) and j+1 in range(len(tablero[i])) and tablero[i+1][j+1] == turno:
        con += 1
        if i+2 in range(len(tablero)) and j+2 in range(len(tablero[i])) and tablero[i+2][j+2] == turno:
            con += 1
            if i + 3 in range(len(tablero)) and j+3 in range(len(tablero[i])) and tablero[i+3][j+3] == turno:
                con += 1
                return con
            else:
                con = 1
        else:
            con = 1
    else:
        con = 1

    if i-1 in range(len(tablero)) and j+1 in range(len(tablero[i])) and tablero[i-1][j+1] == turno:
        con += 1
        if i-2 in range(len(tablero)) and j+2 in range(len(tablero[i])) and tablero[i-2][j+2] == turno:
            con += 1
            if i-3 in range(len(tablero)) and j+3 in range(len(tablero[i])) and tablero[i-3][j+3] == turno:
                con += 1
                return con
            elif i+1 in range(len(tablero)) and j-1 in range(len(tablero[i])) and tablero[i+1][j-1] == turno:
                con += 1
                return con
            else:
                con = 1
        elif i+1 in range(len(tablero)) and j-1 in range(len(tablero[i])) and tablero[i+1][j-1] == turno:
            con += 1
            if i+2 in range(len(tablero)) and j-2 in range(len(tablero[i])) and tablero[i+2][j-2] == turno:
                con += 1
                return con
            else:
                con = 1
        else:
            con = 1
    elif i+1 in range(len(tablero)) and j-1 in range(len(tablero[i])) and tablero[i+1][j-1] == turno:
        con += 1
        if i+2 in range(len(tablero)) and j-2 in range(len(tablero[i])) and tablero[i+2][j-2] == turno:
            con += 1
            if i + 3 in range(len(tablero)) and j-3 in range(len(tablero[i])) and tablero[i+3][j-3] == turno:
                con += 1
                return con
            else:
                con = 1
        else:
            con = 1
    else:
        con = 1

    return con
