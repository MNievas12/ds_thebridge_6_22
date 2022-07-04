import functions as f


tablero = f.inicializa_tablero()

lista_barcos = [f.barco_aleatorio(2), f.barco_aleatorio(4)]

tablero = f.colocar_barcos(tablero, lista_barcos)

print('variable_1')

tablero = f.disparo(tablero, (3,4))

print(tablero)
