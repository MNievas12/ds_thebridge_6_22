import numpy as np

def barco_aleatorio(eslora):
    
    fila = np.random.randint(10)
    columna = np.random.randint(10)
    coordenadas_barco = [(fila, columna)]
    orien = np.random.choice(["Norte", "Sur", "Este", "Oeste"])

    while len(coordenadas_barco) < eslora:
        if orien == "Norte":
            fila = fila - 1
        if orien == "Sur":
            fila = fila + 1
        if orien == "Este":
            columna = columna + 1
        if orien == "Oeste":
            columna = columna - 1
        
        coordenadas_barco.append((fila, columna))
    
    return coordenadas_barco


def colocar_barco(tablero, barco):

    for elem in barco:
        print("Colocando barco en posicion", elem)
        tablero[elem] = "O"
    return tablero


def colocar_barcos(tablero, barcos):

    for barco in barcos:
        tablero = colocar_barco(tablero, barco)
    return tablero


def disparo(tablero, coordenada):

    if tablero[coordenada] == "O":
        print("Tocado")
        tablero[coordenada] = "X"
    else:
        print("Agua")
        tablero[coordenada] = "-"
    return tablero


def inicializa_tablero():

    tablero = np.full((10,10), fill_value=" ")
    return tablero